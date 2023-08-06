import zipfile
import os
from PIL import Image
from pprint import pprint
from functools import lru_cache


class Myzipfile(object):
    def __init__(self, path):
        assert os.path.exists(path)
        self.zf = zipfile.ZipFile(path)
        self.entrys = self.zf.infolist()

    # read content from specific extensions
    def read_images(self, ext=['.jpg', '.png', '.jpeg']):
        ret = []
        for entry in self.entrys:
            file_name = entry.filename
            if any([file_name.endswith(x) for x in ext]):
                ret.append(Image.open(self.zf.open(entry)))
        return ret

    # read paths from specific extensions
    def spec_ext_paths(self, ext=['.jpg', '.png', '.jpeg']):
        ret = []
        for entry in self.entrys:
            file_name = entry.filename
            if any([file_name.endswith(x) for x in ext]):
                ret.append(file_name)
        return ret

    # read content from filename
    @lru_cache(maxsize=2048)
    def read_file(self, file_name):
        return self.zf.open(file_name)

    def __del__(self):
        self.zf.close()


if __name__ == '__main__':
    path = os.path.join('D:\HairReconstruction', 'data', 'trainB_align.zip')
    zf = Myzipfile(path)
    paths = zf.spec_ext_paths('.mat')