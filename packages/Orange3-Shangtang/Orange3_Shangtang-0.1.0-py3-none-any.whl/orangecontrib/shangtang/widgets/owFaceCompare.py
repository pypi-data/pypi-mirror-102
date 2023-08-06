from pathlib import Path

from .utils.utils import *
from .utils.owShangtangApi import ShangtangAPI, ShangtangMixin

from Orange.widgets import gui
from Orange.widgets.utils.signals import Output, Input
from Orange.widgets.settings import Setting, SettingProvider
from PyQt5.QtWidgets import QLineEdit


class FaceCompare(ShangtangMixin, ShangtangAPI):
    name = "人脸对比"
    description = "用于从两张只有一张人脸的图片中获取人脸的脸部特征数据，并对比两张图片中人脸是否为同一个人。"
    icon = "icons/face_compare.png"
    keywords = ['renlian', 'duibi', 'renlianduibi']
    category = 'shangtang'


    class Inputs:
        img_path_1 = Input('图片1路径', Path, default=True)
        img_path_2 = Input('图片2路径', Path, default=True)

    @Inputs.img_path_1
    def set_image1(self, img_path):
        """Set the input image."""
        self.pic_path_1 = self.check_image(img_path)

    @Inputs.img_path_2
    def set_image2(self, img_path):
        """Set the input image."""
        self.pic_path_2 = self.check_image(img_path)

    def check_image(self,img_path):
        if img_path is None or str(img_path) == '':
            self.info_label.setText("没有图片数据")
        else:
            return img_path

    def __init__(self):
        super().__init__()

    

    def run(self):
        # Authentication token request url
        self.token_url = f"https://{self.base_url}/api/common/v1/token"
        # Face Comparison request url
        self.url = f"https://{self.base_url}/api/internal_sdk/v1/face/compare"
        
        self.result.setText(self.get_result())
