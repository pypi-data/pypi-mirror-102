import os
import skimage
import numpy as np
import cv2


def _process_image_or_path(image_or_path):
    '''
    Input: [str path to image | ndarray image with N,H,W,C ]
    Output: H,W,3
    '''
    if isinstance(image_or_path, str):
        try:
            image = skimage.io.imread(image_or_path)
        except IOError:
            print("error opening file :: ", image_or_path)
            return None
    else:
        image = image_or_path

    if image.ndim == 2:
        image = skimage.color.gray2rgb(image)
    elif image.ndim == 4:
        image = image[..., :3]
    return image


def draw_box(self, image_or_path, boxes, show=True, save=False, path=None):
    '''
    Input:
        image_or_path: image or path string
        boxes: [2] or [N, 2]
        show: show or return
    '''
    image = _process_image_or_path(image_or_path)
    if type(boxes) != np.ndarray or type(boxes) != np.array:
        boxes = np.array(boxes)
    if len(boxes.shape) == 1:
        boxes = np.expand_dims(boxes, 0)
    for box in boxes:
        cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 255, 0),
                      2)

    if save:
        cv2.imwrite(path, image)

    if show:
        cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
        cv2.imshow('image', image)
        cv2.waitKey(5000)
        return None
    else:
        return image