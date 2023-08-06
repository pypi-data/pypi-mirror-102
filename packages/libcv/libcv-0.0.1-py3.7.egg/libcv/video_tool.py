import os

import cv2
import numpy as np
from skimage import io
import io_util
from math import floor


def split_video(video_path, dst_dir, from_i=None, to_i=None):
    assert os.path.exists(video_path, )
    os.makedirs(dst_dir, exist_ok=True)
    # create a VideoCapture object and read from input
    cap = cv2.VideoCapture(video_path)
    # Check if camera opened successfully
    if (cap.isOpened() == False):
        print("Error opening video stream of file")
    # Read until video is completed
    count = 0
    while (cap.isOpened()):
        if to_i is not None and count >= to_i: break
        ret, frame = cap.read()
        if from_i is not None and count < from_i: continue
        if ret == True:
            cv2.imwrite(os.path.join(dst_dir, f'{count}.png'), frame)
        else:  # break the loop
            break
        count += 1
    # Release the video capture object
    cap.release()
    # Closes all the frames
    cv2.destroyAllWindows()


class Video(object):
    def __init__(self, fps=15):
        self.fps = fps

    def merge_video(self, images, dst_pth):
        '''
        Images: [image, . . .]
        - Images must have the same shape
        '''
        assert len(images) > 0
        H, W = images[0].shape[:2]
        out = cv2.VideoWriter(dst_pth,
                              cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                              self.fps, (W, H))
        for image in images:
            out.write(image)
        out.release()
        print(f'video are merged: {dst_pth}')

    def read_images(self, src_dir):
        assert os.path.isdir(src_dir)
        path_list = [
            x for x in os.listdir(src_dir)
            if x.endswith('.png') or x.endswith('.jpg')
        ]
        ret = []
        for path in path_list:
            ret.append(io.imread(os.path.join(src_dir, path))[:, :, :3])
        return ret

    @staticmethod
    def split_large_image(image_or_path, len_H, len_W):
        image = io_util._process_image_or_path(image_or_path)
        H, W = image.shape[:2]
        images_list = []
        div_H = floor(H * 1. / len_H)
        div_W = floor(H * 1. / len_W)
        for i in range(len_H):
            for j in range(len_W):
                div_img = image[div_H * i:div_H * (i + 1), div_W * j:div_W *
                                (j + 1)]
                images_list.append(div_img[:, :, ::-1])
                # TODO
                # if div_img.shape[0] != div_H or div_img.shape[1] != div_W:
                #     div_img = np
                # images_list.append(div_img)
        return images_list


if __name__ == '__main__':
    img_pth = 'fit_1.jpg_per.png'
    video = Video(fps=3)
    images = Video.split_large_image(img_pth, 10, 10)
    video.merge_video(images, img_pth.replace('.png', '.avi'))