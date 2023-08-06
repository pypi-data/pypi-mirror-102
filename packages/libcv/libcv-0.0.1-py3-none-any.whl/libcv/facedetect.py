import os

import cv2
import numpy as np
from skimage import color, io
from libcv.comm import io_util


class FD(object):
    def __init__(self, detector='sfd', gpu=False):
        '''
        detector in ['sdf', 'dlib', 'retina', 'facebox'],
        retina face can process batch images
        '''
        self.type = detector
        face_detector_module = __import__('libcv.detection.' + detector,
                                          globals(), locals(), [detector], 0)
        if detector == 'retina':
            self.face_detector = face_detector_module.RetinaFace(
                gpu_id=-1 if not gpu else 0)
        elif detector == 'facebox':
            self.face_detector = face_detector_module.FaceBoxes()
        else:
            self.face_detector = face_detector_module.FaceDetector(
                device='cpu' if not gpu else 'cuda')

    def _get_detects(self, image_or_path):
        image = io_util._process_image_or_path(image_or_path)
        detected_faces = self.face_detector.detect_from_image(
            image[..., ::-1].copy())
        if len(detected_faces) == 0:
            print('Warning: No faces were detected.')
            return None
        return detected_faces

    def draw_box(self, image_or_path, boxes, show=True, save=False, path=None):
        '''
        Input:
            image_or_path: image or path string
            boxes: [2] or [N, 2]
            show: show or return
        '''

        image = io_util._process_image_or_path(image_or_path)
        if type(boxes) != np.ndarray or type(boxes) != np.array:
            boxes = np.array(boxes)
        if len(boxes.shape) == 1:
            boxes = np.expand_dims(boxes, 0)
        for box in boxes:
            cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]),
                          (0, 255, 0), 2)

        if save:
            cv2.imwrite(path, image)

        if show:
            cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('image', image)
            cv2.waitKey(5000)
            return None
        else:
            return image

    def __call__(self, image_or_path):
        if self.type in ['retina', 'facebox']:
            if isinstance(image_or_path, str):
                image_or_path = io_util._process_image_or_path(image_or_path)
            return self.face_detector(image_or_path)
        else:
            return self._get_detects(image_or_path)
