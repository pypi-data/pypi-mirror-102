import os

import face_alignment
import matplotlib.pyplot as plt
import numpy as np
from skimage import color, io, transform
from PIL import Image
from libcv.comm import io_util


class FA(object):
    def __init__(self, n_dim=2, flip=False, gpu=False):
        assert n_dim in [2, 3], 'n_dim must be 2 or 3'
        if n_dim == 2:
            n_dim_type = face_alignment.LandmarksType._2D
        elif n_dim == 3:
            n_dim_type = face_alignment.LandmarksType._3D
        self.Model = face_alignment.FaceAlignment(
            n_dim_type, flip_input=flip, device='cpu' if not gpu else 'cuda')

    def get_landmark(self, image_or_path, detected_faces=None):
        '''
        input: {string or numpy.array or torch.tensor} -- The input image or path to it.
        detected_faces: {list of numpy.array} -- list of bounding boxes, one for each face found
            in the image
        return:  a set of 68 2D or 3D points, one for each image present.
        '''
        points = self.Model.get_landmarks_from_image(image_or_path,
                                                     detected_faces)
        return points

    def draw_points(self, image_or_path, pts):
        '''
        image_or_path: {string or numpy.array or torch.tensor} -- The input image or path to it.
        pts: 
        '''
        image = io_util._process_image_or_path(image_or_path)
        if type(pts) == list:
            pts = np.array(pts)
        pts = np.squeeze(pts)
        print(pts.shape)
        # visualize
        fig = plt.figure(figsize=plt.figaspect(.5))
        ax = fig.add_subplot(1, 2, 1)
        ax.imshow(image)
        ax.plot(pts[0:17, 0],
                pts[0:17, 1],
                marker='o',
                markersize=6,
                linestyle='-',
                color='w',
                lw=2)
        ax.plot(pts[17:22, 0],
                pts[17:22, 1],
                marker='o',
                markersize=6,
                linestyle='-',
                color='w',
                lw=2)
        ax.plot(pts[22:27, 0],
                pts[22:27, 1],
                marker='o',
                markersize=6,
                linestyle='-',
                color='w',
                lw=2)
        ax.plot(pts[27:31, 0],
                pts[27:31, 1],
                marker='o',
                markersize=6,
                linestyle='-',
                color='w',
                lw=2)
        ax.plot(pts[31:36, 0],
                pts[31:36, 1],
                marker='o',
                markersize=6,
                linestyle='-',
                color='w',
                lw=2)
        ax.plot(pts[36:42, 0],
                pts[36:42, 1],
                marker='o',
                markersize=6,
                linestyle='-',
                color='w',
                lw=2)
        ax.plot(pts[42:48, 0],
                pts[42:48, 1],
                marker='o',
                markersize=6,
                linestyle='-',
                color='w',
                lw=2)
        ax.plot(pts[48:60, 0],
                pts[48:60, 1],
                marker='o',
                markersize=6,
                linestyle='-',
                color='w',
                lw=2)
        ax.plot(pts[60:68, 0],
                pts[60:68, 1],
                marker='o',
                markersize=6,
                linestyle='-',
                color='w',
                lw=2)
        ax.axis('off')

        ax.set_xlim(ax.get_xlim()[::-1])
        plt.show()

    @staticmethod
    def get_five_points(points):
        '''
        return left_eye , right_eye , nose , left_mouth , right_mouth points
        '''
        if isinstance(points, list):
            points = np.array(points)
        if len(points.shape) == 3:
            points = points[0]
        left_eye_i = list(range(36, 42))
        right_eye_i = list(range(42, 48))
        nose_i = [30]
        left_mouth = [48]
        right_mouth = [54]

        def _get_mean_points(points_i):
            sum_pos = np.zeros(2)
            for index in points_i:
                sum_pos += points[index]
            return sum_pos / len(points_i)

        positions = np.array([
            _get_mean_points(x) for x in
            [left_eye_i, right_eye_i, nose_i, left_mouth, right_mouth]
        ])
        print(positions.shape)
        return positions

    @staticmethod
    def extract_image_chip(img,
                           points,
                           out_size=256,
                           padding=0,
                           ext_pts=None,
                           re_tform=None,
                           shift_y=0):
        '''
            crop and align face to the mean face of below folder:
                "/mnt/d1p8/ming/FaceData/AlignmentA/'
        --------
            img: numpy array , rgb from skimage , [h ,w , c]
            points: numpy array, [5 ,2]
            out_size: default 256
            ext_pts: extra points that need to be transformed
            return: croped image
        --------
        '''
        ratio = 256. / out_size
        h, w = img.shape[:2]
        # padding = 0 if padding <= 0 else padding
        mean_face_x = [
            103.41464928, 153.91216895, 127.90328177, 105.73770997,
            151.42750902
        ]
        mean_face_y = [
            118.68984714, 118.68640815, 151.95155047, 174.6447198, 174.36142211
        ]
        mean_face_x = [x / out_size / ratio for x in mean_face_x]
        mean_face_y = [y / out_size / ratio for y in mean_face_y]

        mean_face_y = [y + shift_y for y in mean_face_y]
        # mean_face_x = [0.224152, 0.75610125, 0.490127, 0.254149, 0.726104]
        # mean_face_y = [0.2119465, 0.2119465, 0.628106, 0.780233, 0.780233]

        from_points = []
        to_points = []
        for i in range(points.shape[0]):
            x = (padding + mean_face_x[i]) / (2 * padding + 1) * out_size
            y = (padding + mean_face_y[i]) / (2 * padding + 1) * out_size
            to_points.append([x, y])
            from_points.append(points[i])
        dst = np.array(to_points, dtype=np.float32).reshape(5, 2)
        src = np.array(from_points, dtype=np.float32).reshape(5, 2)
        tform = transform.SimilarityTransform()
        tform.estimate(src, dst)
        warped = transform.warp(img,
                                tform.inverse,
                                output_shape=(out_size, out_size))
        fa_points = tform(points)
        if ext_pts is not None:
            ext_pts = tform(ext_pts)
            return warped, fa_points, ext_pts
        elif re_tform is not None:
            return warped, fa_points, tform
        else:
            return warped, fa_points

    @staticmethod
    def plot_points(surface, points, N=False):
        '''
        surface: face image
        points: [N , 2] numpy array , landmark points
        N: if draw number of landmark
        '''
        if isinstance(points, list):
            points = np.array(points)
        if len(points.shape) == 3:
            points = points[0]
        assert points.shape[1] == 2
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.imshow(surface)
        ax.scatter(points[:, 0], points[:, 1], marker='.', color='r')
        if N:
            for i in range(points.shape[0]):
                plt.annotate(str(i), points[i])
        plt.show()

    @staticmethod
    def plot_landmarks(frame, landmarks, dpi=100):
        """
        Creates an RGB image with the landmarks. The generated image will be of the same size as the frame where the face
        matching the landmarks.
        The image is created by plotting the coordinates of the landmarks using matplotlib, and then converting the
        plot to an image.
        Things to watch out for:
        * The figure where the landmarks will be plotted must have the same size as the image to create, but matplotlib
        only accepts the size in inches, so it must be converted to pixels using the DPI of the screen.
        * A white background is printed on the image (an array of ones) in order to keep the figure from being flipped.
        * The axis must be turned off and the subplot must be adjusted to remove the space where the axis would normally be.
        :param frame: Image with a face matching the landmarks.
        :param landmarks: Landmarks of the provided frame,
        :return: RGB image with the landmarks as a Pillow Image.
        """
        fig = plt.figure(figsize=(frame.shape[1]/dpi, frame.shape[0]/dpi), dpi = dpi)
        ax = fig.add_subplot(1,1,1)
        ax.imshow(np.ones(frame.shape))
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

        #chin
        ax.plot(landmarks[0:17,0],landmarks[0:17,1],marker='',markersize=5,linestyle='-',color='green',lw=2)
        #left and right eyebrow
        ax.plot(landmarks[17:22, 0], landmarks[17:22, 1], marker='', markersize=5, linestyle='-', color='orange', lw=2)
        ax.plot(landmarks[22:27, 0], landmarks[22:27, 1], marker='', markersize=5, linestyle='-', color='orange', lw=2)
        #nose
        ax.plot(landmarks[27:31,0],landmarks[27:31,1],marker='',markersize=5,linestyle='-',color='blue',lw=2)
        ax.plot(landmarks[31:36,0],landmarks[31:36,1],marker='',markersize=5,linestyle='-',color='blue',lw=2)
        #left and right eye
        ax.plot(landmarks[36:42, 0], landmarks[36:42, 1], marker='', markersize=5, linestyle='-', color='red', lw=2)
        ax.plot(landmarks[[36,41],0],landmarks[[36,41],1],marker='',markersize=5,linestyle='-',color='red',lw=2)
        ax.plot(landmarks[42:48, 0], landmarks[42:48, 1], marker='', markersize=5, linestyle='-', color='red', lw=2)
        ax.plot(landmarks[[42,47],0],landmarks[[42,47],1],marker='',markersize=5,linestyle='-',color='red',lw=2)
        #outer and inner lip
        ax.plot(landmarks[48:60, 0], landmarks[48:60, 1], marker='', markersize=5, linestyle='-', color='purple', lw=2)
        ax.plot(landmarks[[48,59],0],landmarks[[48,59],1],marker='',markersize=5,linestyle='-',color='purple',lw=2)
        ax.plot(landmarks[60:68, 0], landmarks[60:68, 1], marker='', markersize=5, linestyle='-', color='pink', lw=2)
        ax.plot(landmarks[[60,67],0],landmarks[[60,67],1],marker='',markersize=5,linestyle='-',color='pink',lw=2) 
        ax.axis('off')

        fig.canvas.draw()

        line_draw = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        line_draw = line_draw.reshape(fig.canvas.get_width_height()[::-1] + (3,))

        plt.close(fig)
        return frame, line_draw


if __name__ == '__main__':
    fa = FA()
    root = os.path.dirname(__file__)
    file_path = os.path.join(root, 'example/input/000001.jpg')
    img = io.imread(file_path)
    pts = fa.get_landmark(file_path)
    FA.plot_points(img, pts, True)
    # fa.draw_points(file_path, pts)
    five_pts = FA.get_five_points(pts)
    FA.plot_points(img, five_pts)
    with open("example/output/000001.txt", 'w') as f:
        for pt in pts[0]:
            f.write(f"{pt[0]} {pt[1]}\n")
