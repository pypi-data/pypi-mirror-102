import torch
import cv2
import functools
import sys
sys.path.append('..')
import math
from skimage import color
import numpy as np
import torch.nn.functional as F
import matplotlib.pyplot as plt


class OrientationMap(object):
    def __init__(self, device, dtype=torch.float32):
        self.device = device
        self.dtype = dtype

    def get_orient_map(self, x, out_channels=180, thres=0., vis=False):
        '''
        x: B C H W
        dxdy: B 2 H W
        thetas: B H W
        '''
        _, _, H, W = x.size()
        ratio = H / 850 if H < W else W / 850
        lambd = 4
        sigma = 1.8
        gabor_ac = self.gabor_conv2d(x, out_channels, sigma=sigma, lambd=lambd)
        thetas, confidence, intensity = self._orientation(gabor_ac)
        zeros_pl = torch.zeros_like(thetas).to(self.device)
        threshold = torch.where(intensity > thres, torch.ones_like(intensity),
                                torch.zeros_like(intensity))
        orient_mask = threshold > thres
        # get dx dy
        dx = torch.where(orient_mask, torch.cos(thetas), zeros_pl)
        dy = torch.where(orient_mask, torch.sin(thetas), zeros_pl)
        dxdy = torch.stack([dx, dy], dim=1)
        # render image
        if vis:
            o_map = OrientationMap.render_orientation(dxdy[0],
                                                      confidence=threshold[0])
            plt.figure(figsize=(16, 16))
            plt.imshow(o_map)
            plt.show()
        return dxdy, thetas, intensity
        # self.iterative_refinement(confidence, thetas)

    def iterative_refinement(self, tensor_image, thetas, n_iter=3, thres=0):
        for i in range(n_iter):
            if len(tensor_image.size()) == 3:
                tensor_image = tensor_image.unsqueeze(1)
            gabor_ac = self.gabor_conv2d(tensor_image, 18)
            dxy, thetas, confidence, intensity = self._orientation(gabor_ac)
            o_map = OrientationMap.render_orientation(dxy[0].permute(1, 2, 0),
                                                      thetas[0])
            plt.figure(figsize=(16, 8))
            plt.imshow(o_map)
            plt.show()

    def _orientation(self, gabor_ac):
        '''
        gabor_ac: B C H W
        return:
            dxdy: B 2 H W
            thetas: B H W
            confidence: B H W
        '''
        _, out_channels, _, _ = gabor_ac.size()
        gabor_max, max_indices = torch.max(gabor_ac, dim=1, keepdim=False)

        # get intensity
        intensity = torch.sqrt(
            torch.where(gabor_max > 0., gabor_max,
                        torch.zeros_like(gabor_max)))
        # get confidence
        confidence = self._confidence(gabor_ac)

        # get thetas
        thetas = max_indices.type(
            gabor_ac.dtype) * math.pi / out_channels  # 0~pi
        return thetas, confidence, intensity

    def gabor_conv2d(self,
                     x,
                     out_channels,
                     ksize=6,
                     sigma=1.8,
                     lambd=4,
                     gamma=3. / 4.):
        '''
        - x: B C H W
        return:
        - gabor_ac: B out_channels H W
        '''
        B, C, H, W = x.size()
        kernel = self._kernel(C, ksize, sigma, lambd, gamma)
        # padding images
        max_len = math.ceil(math.sqrt((H / 2.)**2 + (W / 2.)**2))
        pad_h, pad_w = math.ceil(max_len - H / 2.), math.ceil(max_len - W / 2.)
        dst_H, dst_W = pad_h * 2 + H, pad_w * 2 + W
        new_x = torch.zeros((B, C, dst_H, dst_W)).type(x.dtype).to(self.device)
        new_x[:, :, pad_h:pad_h + H, pad_w:pad_w + W] = x
        # create mesh grid
        yv, xv = torch.meshgrid(torch.arange(dst_H), torch.arange(dst_W))
        xv = xv.contiguous().float().view(-1, 1).to(self.device)
        yv = yv.contiguous().float().view(-1, 1).to(self.device)
        mesh_xyz = torch.cat((xv, yv, torch.ones_like(xv)), dim=1)
        gabor_ac = [None] * out_channels
        for i in range(out_channels):
            # rotate images
            M, M_inv = self._rotate_Matrix(dst_H // 2, dst_W // 2,
                                           i * 180. / out_channels)
            grid = torch.matmul(mesh_xyz, M.t())  # N x 2
            grid_x = grid[:, 0].view(1, dst_H, dst_W) / dst_W * 2 - 1.
            grid_y = grid[:, 1].view(1, dst_H, dst_W) / dst_H * 2 - 1.
            grid = torch.stack((grid_x, grid_y), dim=-1).repeat(B, 1, 1, 1)
            rot_x = F.grid_sample(new_x, grid)
            response = F.conv2d(rot_x,
                                kernel,
                                padding=(kernel.size(-1) - 1) // 2)
            grid = torch.matmul(mesh_xyz, M_inv.t())  # N x 2
            grid_x = grid[:, 0].view(1, dst_H, dst_W) / dst_W * 2 - 1.
            grid_y = grid[:, 1].view(1, dst_H, dst_W) / dst_H * 2 - 1.
            grid = torch.stack((grid_x, grid_y), dim=-1).repeat(B, 1, 1, 1)
            response = F.grid_sample(response, grid)
            gabor_ac[i] = response[:, :, pad_h:pad_h + H, pad_w:pad_w + W]
        return torch.cat(gabor_ac, dim=1)

    @staticmethod
    def render_orientation(dxdy, thetas=None, confidence=None, rainbow=True):
        '''
        dxdy: H W 2
        thetas: H W
        '''
        dxdy = dxdy.permute(1, 2, 0).cpu().numpy()
        confidence = confidence.cpu().numpy()
        do = np.ones_like(dxdy[:, :, 0], dtype=np.float32)
        if confidence is not None:
            confidence = confidence / np.max(confidence)
        if thetas is not None:
            HSV = np.stack([
                thetas / math.pi, do,
                confidence if confidence is not None else do
            ], -1)
            RGB = color.hsv2rgb(HSV) * 255
        else:
            assert len(dxdy.shape) == 3 and dxdy.shape[-1] == 2
            # dx :[-1 , 1] , dy: [0 , 1]
            dx, dy = dxdy[:, :, 0], dxdy[:, :, -1]
            if rainbow:
                HSV = np.stack([
                    np.arccos(dx) / math.pi, do,
                    confidence if confidence is not None else do
                ], -1)
                RGB = color.hsv2rgb(HSV) * 255
            else:
                RGB = np.stack([do, dy, dx / 2 + .5], -1) * 255

        return RGB.astype(np.uint8)

    def _confidence(self, gabor_ac):
        ''' 
        gabor_ac: B C H W
        '''
        b, c, h, w = gabor_ac.size()
        gabor_max, gabor_max_indexs = torch.max(input=gabor_ac,
                                                dim=1,
                                                keepdim=True)
        gabor_max_theta = gabor_max_indexs.type(gabor_ac.dtype) * math.pi / c
        gabor_per_theta = torch.tensor(list(
            range(c)), dtype=gabor_ac.dtype).to(self.device).repeat(
                b, h, w, 1).permute(0, 3, 1, 2) * math.pi / c
        min_a = (gabor_max_theta - gabor_per_theta).abs()
        min_b = (gabor_max_theta - gabor_per_theta + math.pi).abs()
        min_c = (gabor_max_theta - gabor_per_theta - math.pi).abs()
        degree_diff = torch.min(min_a, min_b)
        degree_diff = torch.min(min_c, degree_diff)
        ac_diff = (gabor_max - gabor_ac)**2
        confidence = torch.sum(torch.sqrt(torch.mul(degree_diff, ac_diff)),
                               dim=1,
                               keepdim=False) / c
        return confidence

    @functools.lru_cache()
    def _kernel(self, C, ksize, sigma, lambd, gamma):
        kernel = cv2.getGaborKernel((ksize, ksize),
                                    sigma,
                                    math.pi / 2,
                                    lambd,
                                    gamma,
                                    psi=0,
                                    ktype=cv2.CV_32F)
        kernel = torch.from_numpy(kernel).type(self.dtype).to(
            self.device).unsqueeze(0).unsqueeze(0).repeat(1, C, 1, 1)
        return kernel

    @functools.lru_cache()
    def _rotate_Matrix(self, h, w, theta):
        M = cv2.getRotationMatrix2D((h, w), theta, 1)
        M_inv = cv2.getRotationMatrix2D((h, w), -theta, 1)
        M = torch.from_numpy(M).type(self.dtype).to(self.device)
        M_inv = torch.from_numpy(M_inv).type(self.dtype).to(self.device)
        return M, M_inv


if __name__ == '__main__':
    image = cv2.imread('scripts\\circle.png')[:, :, ::-1] / 255.0
    image = torch.from_numpy(image).unsqueeze(0).permute(0, 3, 1, 2).float()
    Gabor = OrientationMap(torch.device('cpu'))
    Gabor.get_orient_map(image, 18, 0., True)
