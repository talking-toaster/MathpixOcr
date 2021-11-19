import base64
import time
import requests


class MathpixOcr:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password
        self.session = requests.session()

    def login(self):
        headers = {
            'authority': 'api.mathpix.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '"Microsoft Edge";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json;charset=UTF-8',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://accounts.mathpix.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://accounts.mathpix.com/',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        }
        loginData = '{"email":"'+self.email+'","password":"'+self.password+'"}'
        loginRes = self.session.post(
            'https://api.mathpix.com/v1/user/login', headers=headers, data=loginData)
        return loginRes

    def getUserInfo(self):
        userRes = self.session.get('https://api.mathpix.com/v1/user')
        return userRes

    def getImageData(self, path):
        with open(path, "rb") as f:
            b64data = base64.b64encode(f.read()).decode()
            postData = '{"src":"data:image/png;base64,'+b64data + \
                '","config":{"math_inline_delimiters":["$","$"],"math_display_delimiters":["$$\\n","\\n$$"],"rm_spaces":false,"rm_newlines":false,"rm_fonts":false,"ocr_version":2},"metadata":{"input_type":"web_editor"}}'
            return postData

    def isonline(self):
        if self.getUserInfo().status_code == 200:
            return True
        else:
            return False

    def ocr(self, imagePath):
        ocrRes = self.session.post(
            'https://api.mathpix.com/v1/snips', data=self.getImageData(imagePath))
        return ocrRes
