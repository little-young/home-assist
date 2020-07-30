# -*- coding: utf-8 -*-
# @file  : token_verify
# @author: xiaoyang.wang
# @date  : 2020/7/25
from flask import request, jsonify, current_app
from itsdangerous import TimedJSONWebSignatureSerializer
import functools
from homeassist.config import ReturnCode,SECRET_KEY


# 第一个参数是内部的私钥
# 第二个参数是有效期(秒)
_s = TimedJSONWebSignatureSerializer(SECRET_KEY, expires_in=3600)

def create_token(id,type):
    '''
    生成token
    :param id:mem_id,user_id等
    :return: token
    '''
    # 接收用户id转换与编码
    token = _s.dumps({"id": id, "type": type}).decode("utf8")
    return token

def verify_token(token):
    '''
    校验token
    :param token:
    :return: 用户信息 or None
    '''
    try:
        # 转换为字典
        data = _s.loads(token)
    except Exception:
        return None
    return data


def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            # 在请求头上拿到token
            token = request.headers["token"]
        except Exception:
            # 没接收的到token,给前端抛出错误
            return jsonify(code=ReturnCode.FAIL.value, msg='缺少参数token')

        try:
            _s.loads(token)
        except Exception:
            return jsonify(code=ReturnCode.FAIL.value, msg="登录已过期")

        return view_func(*args, **kwargs)

    return verify_token

# from homeassist.util import cache
# def get_token(username):
#     '''
#     如果token存在且未过期，返回token
#     else:生成新token
#     :param username:
#     :return: token
#     '''
#     token = cache.get(username, CacheDataBase.MEM_DB)
#     if not token:
#         rand_value = str(random.choice(range(0, 100)))
#         token = hashlib.md5((username + rand_value).encode()).hexdigest()
#         cache.set(username, token, CacheDataBase.MEM_DB_EXP_SECS, CacheDataBase.MEM_DB)
#     return token
