import random
import string
from datetime import datetime

import redis
from flask import current_app, app


def limit_frequency(original_function, redis_instance):
    def wrapper_function(phone, template_param):
        limit_sms_frequency(phone, redis_instance)
        # 调用原始函数
        original_function(phone, template_param)

    return wrapper_function


def create_redis_client():
    r = redis.Redis(
        host=current_app.config.get("SMS_REDIS_HOST"),
        port=current_app.config.get("SMS_REDIS_PORT"),
        db=current_app.config.get("SMS_REDIS_DB"),
        password=current_app.config.get("SMS_REDIS_PASSWORD"),
    )

    return r


# 生成验证码
def generate_verification_code():
    characters = string.digits  # 使用数字作为验证码的字符集合
    code = ''.join(random.choice(characters) for _ in range(4))  # 从字符集合中随机选择4个字符
    return code


# 限制短信频率
def limit_sms_frequency(phone, redis_instance):
    # 设置限制，例如每分钟只能发送一次
    limit = 60  # 秒
    key = "sms_rate_limit:{phone}".format(phone=phone)

    if redis_instance.exists(key):
        return False

    # 设置 Redis 键的过期时间来限制发送频率
    redis_instance.setex(key, limit, 1)

    # 设置每天最大发送次数
    max_daily_limit = 5
    current_date = datetime.now().strftime("%Y-%m-%d")
    key = "sms_daily_limit:{phone_number}:{current_date}".format(phone_number=phone, current_date=current_date)

    # 获取当前手机号今天已发送的次数
    current_count = redis_instance.get(key)
    if current_count is None:
        # 如果还没有发送记录，设置计数为1，并设置过期时间为到今天结束
        ttl = 86400 - datetime.now().second - datetime.now().minute * 60 - datetime.now().hour * 3600
        redis_instance.setex(key, ttl, 1)
        return True
    else:
        current_count = int(current_count)
        if current_count >= max_daily_limit:
            # 如果已达到或超过每天的限制，则不能发送
            return False
        else:
            # 如果没有达到每天的限制，增加发送次数
            redis_instance.incr(key)
            return True
