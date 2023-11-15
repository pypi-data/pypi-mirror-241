import redis
from flask import current_app, app


def limit_frequency(original_function):
    def wrapper_function(*args, **kwargs):
        # # 在调用原始函数之前执行的操作
        # print("装饰器操作：在函数调用之前")

        """
              频率限制
              :return:
        """

        with current_app.app_context():

            if current_app.SMS_REDIS is None:
                current_app.SMS_REDIS = create_redis_client()
        r = current_app.SMS_REDIS

        d = kwargs.get("d")
        phone = d.get("phone_numbers")

        # 从Redis中获取当前手机号已发送的短信次数
        sms_count = r.get(phone)

        if sms_count is None:
            # 如果键不存在，则将短信次数设置为1，并设置过期时间为TIME_WINDOW
            r.setex(phone, 60 * 60 * 24, 1)
        elif int(sms_count) < current_app.config.get("SMS_PHONE_MAX_COUNT_PER_DAY"):
            # 如果短信次数未达到限制，则增加短信次数
            r.incr(phone)
        else:
            return "短信发送过于频繁，请稍后再试"

        # 调用原始函数
        original_function()

        # # 在调用原始函数之后执行的操作
        # print("装饰器操作：在函数调用之后")

    return wrapper_function


def create_redis_client():
    r = redis.Redis(
        host=current_app.config.get("SMS_REDIS_HOST"),
        port=current_app.config.get("SMS_REDIS_PORT"),
        db=current_app.config.get("SMS_REDIS_DB"),
        password=current_app.config.get("SMS_REDIS_PASSWORD"),
    )

    return r
