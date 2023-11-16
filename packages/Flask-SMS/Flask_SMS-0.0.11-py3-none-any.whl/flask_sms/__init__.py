"""
 Flask-SMS
 # ~~~~~~~~~~~~~~ 
 flask 短信 扩展
 Flask SMS extension
 :copyright: (c) 2023.11 by 浩. 
 :license: GPL, see LICENSE for more details.
"""
import os

import flask_limiter
from flask import current_app

from .aliyun_send import Sample

from .utils import limit_frequency, create_redis_client, generate_verification_code


class SMS(object):
    def __init__(self, app=None, **kwargs):
        if app is not None:
            print("init_app")
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        # 兼容 0.7 以前版本
        if not hasattr(app, 'extensions'):
            app.extensions = {}

        # 在 app 应用中存储所有扩展实例, 可验证扩展是否完成实例化
        app.extensions['sms'] = self

        # 扩展配置， 初始化后添加到 app.config 中, 以 SHARE_ 开头避免冲突
        app.config.setdefault('SMS_REDIS_HOST', '127.0.0.1')
        app.config.setdefault('SMS_REDIS_PORT', 6379)
        app.config.setdefault('SMS_REDIS_DB', 0)
        app.config.setdefault('SMS_REDIS_PASSWORD', None)
        app.config.setdefault('SMS_REDIS_INSTANCE', None)

        app.config.setdefault('SMS_PHONE_MAX_COUNT_PER_DAY', 5)
        app.config.setdefault('SMS_CODE_EXPIRATION_TIME', 60 * 5)

        # 设置 Redis 键的过期时间来限制发送频率
        app.config.setdefault('SMS_RATE_LIMIT', 60)
        # 设置每天最大发送次数
        app.config.setdefault('SMS_DAILY_LIMIT', 5)

        # 设置阿里云短信参数
        # 短信签名名称
        app.config.setdefault('SMS_ALIYUN_SMS_SIGN_NAME', None)
        # 短信模板Code
        app.config.setdefault('SMS_ALIYUN_SMS_TEMPLATE_CODE', 1)

        # 设置阿里云短信 AccessKey
        app.config.setdefault('SMS_ALIYUN_ACCESS_KEY_ID', '')
        app.config.setdefault('SMS_ALIYUN_ACCESS_KEY_SECRET', '')



    @staticmethod
    def send_aliyun_sms(phone, template_param):
        """
        发送阿里云短信

        """
        d = {

            "phone": phone,
            # TemplateParam 短信模板变量对应的实际值
            "template_param": template_param
        }

        return Sample.main(d)

    @staticmethod
    def code():

        return generate_verification_code()




