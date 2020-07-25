# -*- coding: utf-8 -*-
# @file  : auth
# @author: xiaoyang.wang
# @date  : 2020/7/11

from flask import Blueprint, jsonify
from flask import flash
from flask import request
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from homeassist.config import ReturnCode
from homeassist.db import get_mysql_db, serialize_row

from homeassist.common import token

# to do
## 加上物业公司权限管理

api_auth_bp = Blueprint("api.member", __name__, url_prefix="/api/member")

MEM_ROLE_DICT = {
    1: "admin",
    11: "manager",
    12: "staff",
    99: "visitor"
}

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
            return jsonify(code=ReturnCode.SUCCESS.value,
                           data={"token": token.create_token(mem["id"], "member")})
        flash(err)
        return jsonify(code=ReturnCode.FAIL.value, msg=err)


@api_auth_bp.route("/regist_staff", methods=("GET", "POST", "HEAD", "OPTIONS"))
@token.login_required
def regist_staff():
    if request.method == "POST":
        # name,property_id,role=12
        # create_time,update_time解决方案
        data = request.get_json()
        name = data["name"]
        property_id = data["property_id"]
        db_conn = get_mysql_db()
        err = None

        if (db_conn.execute("SELECT id FROM mvp.t_member WHERE name = ?", (name,)).fetchone()
                is not None
        ):
            err = "User {0} is already registered.".format(name)

        if err is None:
            db_conn.execute(
                "INSERT INTO mvp.t_member (name, password, role, property_id) VALUES (?, ?, ?, ?)",
                (name, generate_password_hash("123456"), 12, property_id),
            )
            db_conn.commit()

            return jsonify(code=ReturnCode.SUCCESS.value, msg="")

        flash(err)
        return jsonify(code=ReturnCode.FAIL.value, msg=err)

@api_auth_bp.route("/mem_list", methods=("GET", "POST", "HEAD", "OPTIONS"))
@token.login_required
def mem_list():
    db_conn = get_mysql_db()
    mems = db_conn.execute(
        "SELECT id, name, nick_name, role, create_time"
        " FROM mvp.t_member "
        " ORDER BY id ASC"
    ).fetchall()
    mems = serialize_row(mems)
    return jsonify(code=ReturnCode.SUCCESS.value,
                   data={"member":mems})


@api_auth_bp.route("/logout", methods=("GET", "POST", "HEAD", "OPTIONS"))
def logout():
    return jsonify(code=ReturnCode.SUCCESS.value)

@api_auth_bp.route("/mem_modify_pwd", methods=("GET", "POST", "HEAD", "OPTIONS"))
@token.login_required
def mem_modify_pwd():
    if request.method == "POST":
        data = request.get_json()
        mem_id = data["id"]
        pwd = data["password"]
        new_pwd = data["new_password"]
        db_conn = get_mysql_db()

        err = None

        mem = db_conn.execute(
            "SELECT id FROM mvp.t_member WHERE id = ? AND password = ?",
            (mem_id, generate_password_hash(pwd),)
        ).fetchone()

        if mem:
            try:
                db_conn.execute("UPDATE mvp.t_member SET password = ? WHERE id = ?",
                                (generate_password_hash(new_pwd), mem_id),)
                db_conn.commit()
            except Exception as e:
                err = str(e)
        else:
            err = "密码错误"
        if err:
            return jsonify(code=ReturnCode.FAIL.value,msg=err)
        else:
            return jsonify(code=ReturnCode.SUCCESS.value)
