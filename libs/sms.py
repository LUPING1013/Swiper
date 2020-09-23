import time
import json
from hashlib import md5
from Swiper import config
import requests

appid = config.SD_APPID
appkey = config.SD_APPKEY
project = config.SD_PROJECT
sign_type = config.SD_SIGN_TYPE
api = config.SD_API

def send_sms(phonenum,vcode):
    args = {
        'appid': appid,     # APPID
        'to': phonenum,  # 手机号
        'project': project,  # 短信模板的 ID
        'vars': json.dumps({'code': vcode}),
        'timestamp': int(time.time()),
        'sign_type': sign_type,
        }

# 计算参数的签名
    sorted_args = sorted(args.items())  # 提取每一项
    args_str = '&'.join([f'{key}={value}' for key, value in sorted_args])  # 对参数排序、组合
    sign_str = f'{appid}{appkey}{args_str}{appid}{appkey}'.encode('utf8')  # 拼接成待签名字符串
    signature = md5(sign_str).hexdigest()  # 计算签名
    args['signature'] = signature

    response = requests.post(api, data=args)

    if response.status_code == 200:
        result = response.json()
        print('短信结果：', result)
        if result.get('status') == 'success':
            return True
    return False
