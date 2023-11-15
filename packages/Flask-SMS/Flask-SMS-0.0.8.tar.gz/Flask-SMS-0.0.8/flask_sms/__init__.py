"""
 Flask-SMS
 # ~~~~~~~~~~~~~~ 
 flask 短信 扩展
 Flask SMS extension
 :copyright: (c) 2023.11 by 浩. 
 :license: MIT, see LICENSE for more details. 
"""

from .aliyun_send import Sample


class SMS(object):
    def __init__(self, app=None,**kwargs):
        if app is not None:
            self.init_app(app,**kwargs)

    def init_app(self, app,**kwargs):
        # 兼容 0.7 以前版本
        if not hasattr(app, 'extensions'):
            app.extensions = {}

        # 在 app 应用中存储所有扩展实例, 可验证扩展是否完成实例化
        app.extensions['sms'] = self

        # 扩展类添加到模板上下文中
        # app.jinja_env.globals['sms'] = self
        # app.context_processor(lambda：{'share'： self})

        # 扩展配置， 初始化后添加到 app.config 中, 以 SHARE_ 开头避免冲突
        app.config.setdefault('SMS_1', '')
        app.config.setdefault('SMS_2', '')





    @staticmethod
    def send_aliyun_sms(d: dict):
        """
        发送阿里云短信
        :param d: 短信参数
        d={
            "sign_name":"",
            "template_code":"",
            "phone_numbers":"",
            "template_param":"",


        }


        """

        return Sample.main(d)
