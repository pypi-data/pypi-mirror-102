import json
import os

import requests

from AnyQt.QtCore import Qt, QPointF, QSize, Signal, QRectF

from Orange.widgets.widget import OWWidget
from Orange.widgets.utils.signals import Output, Input
from Orange.widgets.settings import Setting
from Orange.widgets import gui
from PyQt5.QtWidgets import QLineEdit

from .utils import img_to_base64

class ShangtangAPI():
    """
    使用商汤教育 API 做深度学习预测
    """

    # API calling access key
    ACCESS_KEY_ID = ""
    ACCESS_KEY_SECRET = ""

    def __init__(self):
        self.pic_path_1 = ''
        self.pic_path_2 = ''
        # Authentication token request url
        self.token_url = ""
        # Face Comparison request url
        self.url = ""

    def get_access_token(self):
        # obtain authentication token
        headers = {"languageType": "zh_CHS"}
        token_params = {"accessKeyId": self.ACCESS_KEY_ID,
                        "accessKeySecret": self.ACCESS_KEY_SECRET}
        token_response = requests.get(
            url=self.token_url, headers=headers, params=token_params, verify=False).text
        token = json.loads(token_response).get("data")

        if not token:
            print('无法获取认证token')
        else:
            return token

    def get_result(self):
        token = self.get_access_token()
        # request headers
        headers = {"languageType": "zh_CHS", "X-Authorization": token}
        # request parameters
        params = {'garble': False}

        try:
            base64_img_1 = img_to_base64(self.pic_path_1)
            base64_img_2 = img_to_base64(self.pic_path_2)
            base64_img = base64_img_1 + b"&" + base64_img_2
            base64_files = {'base64Image':(None, base64_img)}
            response = requests.post(url=self.url, headers=headers, data=params, files=base64_files, verify=False).text
            
            return json.loads(response)['errorMsg']
        except:
            return '错误❌: 请加载图片'


            

class ShangtangMixin(OWWidget):
    """
    添加商汤教育深度学习功能
    """
    want_main_area = True

    ACCESS_KEY_ID = Setting('')
    ACCESS_KEY_SECRET = Setting('')

    params = None
    orgnizations = ['深圳信息职业技术学院', '其他']
    orgnization = 0
    
    base_url = '172.16.100.106:9444'

    #
    # class Outputs:
    #     data = Output('预测结果', Table, default=True)

    def __init__(self):
        super().__init__()

        self.response = {}

        self.info_box = gui.widgetBox(self.controlArea, "信息")
        self.info_label = gui.label(self.info_box, self, '使用商汤教育 API (请使用 jpg 或 png 格式图片)')

        self._setup_control_area()

        gui.button(self.controlArea, self, "运行",
                   callback=self.run, autoDefault=True)

        self._setup_main_area()
        # self.response_label = gui.label(self.mainArea, self, '')

    def _setup_main_area(self):

        self.result = gui.label(self.mainArea, self, '')
        self.result.setWordWrap(True)

    def _setup_control_area(self):
        url_setting_box = gui.widgetBox(self.controlArea, "使用单位:") 
        gui.comboBox(
            url_setting_box,
            self,
            'orgnization',
            items=self.orgnizations,
            label='选择使用单位',
            callback=self._set_base_url
        )


        settings_box = gui.widgetBox(self.controlArea, "秘钥设置:")
        appid = gui.lineEdit(
            settings_box,
            self,
            "ACCESS_KEY_ID",
            "输入 AccessKeyId",
            valueType=str,
        )
        appid.setEchoMode(QLineEdit.Password)
        appkey = gui.lineEdit(
            settings_box,
            self,
            "ACCESS_KEY_SECRET",
            "输入 AccessKeySecret",
            valueType=str,
        )
        appkey.setEchoMode(QLineEdit.Password)

        self.additional_controls()

    def additional_controls(self):
        """
        设置每个应用不同的 UI 组件
        """
        pass

    def run(self):
        raise NotImplementedError

    def sizeHint(self):  # pylint: disable=no-self-use
        return QSize(500, 300)


    def _set_base_url(self):
        """
        根据机构选择对应的 url, 其他则为公有云 api
        """
        if self.orgnization == 0:
            self.base_url = '172.16.100.106:9444'
        else:
            self.base_url = 'open.study.sensetime.com'
        
