import os

from flask_sms import SMS

a = {
    "sign_name": "广东硅基数字产业",
    "template_code": "SMS_276255133",
    "phone_numbers": "15119569881",
    "template_param": '',
}
os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'] = 'LTAI5t5ab2xw5mqu7ggb6WHx'
os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET'] = 'MBihnx35M3I0C2pmb67i38uw3TMZ5'
ACCESS_KEY_ID = "LTAI5t5ab2xw5mqu7ggb6WHx"
ACCESS_KEY_SECRET = "MBihnx35M3I0C2pmb67i38uw3TMZ5"
sign_name = "广东硅基数字产业"  #（签名名称）
c=SMS.send_aliyun_sms(a)
print(c)
