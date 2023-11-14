"""
 Flask-SMS
 # ~~~~~~~~~~~~~~ 
 flask 短信 扩展
 Flask SMS extension
 :copyright: (c) 2023.11 by 浩. 
 :license: MIT, see LICENSE for more details. 
"""
import os

from aliyun_send import Sample


class Share(object):
    def __inti__(self, app=None):
        self.init_app(app)

    def init_app(self, app):
        # 兼容 0.7 以前版本
        if not hasattr(app, 'extensions'):
            app.extensions = {}

        # 在 app 应用中存储所有扩展实例, 可验证扩展是否完成实例化
        app.extensions['share'] = self

        # 扩展类添加到模板上下文中
        app.jinja_env.globals['share'] = self
        # app.context\_processor(lambda：{'share'： self})

        # 扩展配置， 初始化后添加到 app.config 中, 以 SHARE\_ 开头避免冲突
        app.config.setdefault('SHARE_SITES', 'weibo,wechat,douban,facebook,twitter,google,linkedin,qq,qzone')
        app.config.setdefault('SHARE_MOBILESITES', 'weibo,douban,qq,qzone')
        app.config.setdefault('SHARE_HIDE_ON_MOBILE', False)
        app.config.setdefault('SHARE_SERVER_LOCAL', False)  # 是否使用内置资源

    def send_aliyun_sms(self, d: dict):

        Sample.main(d)
