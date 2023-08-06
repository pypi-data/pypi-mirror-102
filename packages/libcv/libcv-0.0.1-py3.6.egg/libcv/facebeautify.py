# -*- coding: utf-8 -*-
import requests
import base64
import os
import re
from json import JSONDecoder
from io import BytesIO
from PIL import Image
import time


class FaceBeautifyApi(object):
    http_url = 'https://api-cn.faceplusplus.com/facepp/v1/beautify'
    key = '0NG0RaG8OXM_MjAJgHnkNI_eAbRgdl4V'
    secret = 'WpHf2l41-xMjqcs7SvuVS0xaVdGHGilr'

    @staticmethod
    def beautify(path, save_path=None):
        data = {
            "api_key": FaceBeautifyApi.key,
            "api_secret": FaceBeautifyApi.secret,
        }
        files = {"image_file": open(path, "rb")}
        response = requests.post(FaceBeautifyApi.http_url,
                                 data=data,
                                 files=files)
        req_con = response.content.decode('utf-8')
        req_dict = JSONDecoder().decode(req_con)
        if not 'result' in req_dict.keys():
            print(req_dict['error_message'])
            return None
        else:
            return FaceBeautifyApi.base64_to_image(req_dict['result'],
                                                   image_path=save_path)

    @staticmethod
    def base64_to_image(base64_str, image_path=None):
        base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
        binary_data = base64.b64decode(base64_data)
        img_data = BytesIO(binary_data)
        img = Image.open(img_data)
        if image_path:
            print('save to ', image_path)
            img.save(image_path)
        return img


if __name__ == '__main__':
    dirname = os.path.join('D:\FaceBeauty', 'SCUT_256', 'Images')
    dirname_2 = os.path.join('D:\FaceBeauty', 'SCUT_256', 'ImagesBeauty')
    os.makedirs(dirname_2, exist_ok=True)
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        save_path = os.path.join(dirname_2, name)
        if not os.path.exists(save_path):
            while not FaceBeautifyApi.beautify(path, save_path):
                time.sleep(2)