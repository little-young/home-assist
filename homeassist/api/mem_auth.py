# -*- coding: utf-8 -*-
# @file  : auth
# @author: xiaoyang.wang
# @date  : 2020/7/11

from flask import Blueprint, jsonify
from flask import flash
from flask import request
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from homeassist.config import ReturnCode, CacheDataBase
from homeassist.db import get_mysql_db, serialize_row

import random
import hashlib
from homeassist.util import cache
from homeassist.util.error import Error

# to do
## 加上物业公司权限管理

api_auth_bp = Blueprint("api.mem_auth", __name__, url_prefix="/api/mem_auth")

MEM_ROLE_DICT = {
    1: "admin",
    18: "manager",
    19: "staff",
    99: "visitor"
}


def get_token(username):
    '''
    如果token存在且未过期，返回token
    else:生成新token
    :param username:
    :return: token
    '''
    token = cache.get(username, CacheDataBase.MEM_DB)
    if not token:
        rand_value = str(random.choice(range(0, 100)))
        token = hashlib.md5((username + rand_value).encode()).hexdigest()
        cache.set(username, token, CacheDataBase.MEM_DB_EXP_SECS, CacheDataBase.MEM_DB)
    return token

@api_auth_bp.route("/register", methods=("GET", "POST", "HEAD", "OPTIONS"))
def register():
    if request.method == "POST":
        data = request.get_json()
        name = data["name"]
        pwd = data["password"]
        db_conn = get_mysql_db()
        err = None

        if not name:
            err = "Username is required."
        elif not pwd:
            err = "Password is required."
        elif (
                db_conn.execute("SELECT id FROM mvp.t_member WHERE name = ?", (name,)).fetchone()
                is not None
        ):
            err = "User {0} is already registered.".format(name)

        if err is None:
            # the name is available, store it in the database and go to
            # the login page
            db_conn.execute(
                "INSERT INTO mvp.t_member (username, password) VALUES (?, ?)",
                (name, generate_password_hash(pwd)),
            )
            db_conn.commit()

            return jsonify({
                "code": ReturnCode.SUCCESS.value,
                "data": {
                    "token": get_token(name)
                }
            })

        flash(err)
        return jsonify({
                "code": ReturnCode.FAIL.value,
                "data": {
                    "msg": err
                }
            })
    return jsonify({
        "code": ReturnCode.FAIL.value,
        "data": {
            "msg": ReturnCode.NOT_SUPPORT_MSG.value
        }
    })

@api_auth_bp.route("/add_mem", methods=("GET", "POST", "HEAD", "OPTIONS"))
def add_mem():
    return

@api_auth_bp.route("/staff_authorize", methods=("GET", "POST", "HEAD", "OPTIONS"))
def staff_authorize():
    return

@api_auth_bp.route("/manager_authorize", methods=("GET", "POST", "HEAD", "OPTIONS"))
def manager_authorize():
    return

@api_auth_bp.route("/login", methods=("GET", "POST", "HEAD", "OPTIONS"))
def login():
    if request.method == "POST":
        data = request.get_json()
        name = data["name"]
        pwd = data["password"]
        db_conn = get_mysql_db()
        err = None

        mem = db_conn.execute(
            "SELECT id FROM mvp.t_member WHERE name = ?", (name,)
        ).fetchone()
        if not mem:
            err = f"{name} is not registered."
        elif not check_password_hash(mem["password"], pwd):
            err = "Incorrect password"
        elif mem["role"] == 99:
            err = f"{name} has not permission"
        if err is None:
            # the name is available, store it in the database and go to
            # the login page
            return jsonify({
                "code": ReturnCode.SUCCESS.value,
                "data": {
                    "token": get_token(name)
                }
            })
        flash(err)
        return jsonify({
                "code": ReturnCode.FAIL.value,
                "data": {
                    "msg": err
                }
            })
    return jsonify({
        "code": ReturnCode.FAIL.value,
        "data": {
            "msg": ReturnCode.NOT_SUPPORT_MSG.value
        }
    })

@api_auth_bp.route("/logout", methods=("GET", "POST", "HEAD", "OPTIONS"))
def logout():
    if request.method == "POST":
        data = request.get_json()
        token = data["name"]
        cache.delete(token, CacheDataBase.MEM_DB)
    return jsonify({
        "code": ReturnCode.SUCCESS.value,
        "data": {
            "msg": "Success"
        }
    })

@api_auth_bp.route("/mem_list", methods=("GET", "POST", "HEAD", "OPTIONS"))
def mem_list():
    db_conn = get_mysql_db()
    mems = db_conn.execute(
        "SELECT id, username, role"
        " FROM mvp.t_member  "
        " ORDER BY id ASC"
    ).fetchall()
    mems = serialize_row(mems)
    return jsonify({
        "code": ReturnCode.SUCCESS.value,
        "data": {
            "member": mems
        }
    })
@api_auth_bp.route("/mem_reset", methods=("GET", "POST", "HEAD", "OPTIONS"))
def mem_reset():
    if request.method == "POST":
        data = request.get_json()
        mem_id = data["id"]
        db_conn = get_mysql_db()

        err = None

        try:
            db_conn.execute(
                "UPDATE mvp.t_member SET password = ? WHERE id = ?",
                (generate_password_hash("123456"), mem_id)
            )
            db_conn.commit()
        except:
            err = "fail"

        if not err:
            return jsonify({
                "code": ReturnCode.SUCCESS.value,
                "data": {
                    "msg": "Success"
                }
            })
        else:
            return jsonify({
                "code": ReturnCode.FAIL.value,
                "data": {
                    "msg": err
                }
            })
    return jsonify({
        "code": ReturnCode.FAIL.value,
        "data": {
            "msg": ReturnCode.NOT_SUPPORT_MSG.value
        }
    })