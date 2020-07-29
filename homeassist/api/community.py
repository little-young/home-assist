# -*- coding: utf-8 -*-
# @file  : community
# @author: xiaoyang.wang
# @date  : 2020/7/29
from flask import Blueprint, jsonify
from flask import flash
from flask import request
from sqlalchemy.orm import sessionmaker

from homeassist.config import ReturnCode
from homeassist.db import get_mysql_db, serialize_row

from homeassist.common import token

api_community_bp = Blueprint("api.community", __name__, url_prefix="/api/community")


def get_community_info_func(community_id):
    db_conn = get_mysql_db()
    cmnt = db_conn.execute(
        "SELECT id as community_id,community_name,property_id,status,"
        " address,contact_name,contact_number,create_time"
        " FROM mvp.t_community_base "
        " WHERE id=? and is_delete=0",
        (community_id,)
    ).fetchone()
    cmnt = serialize_row(cmnt)
    return cmnt

@api_community_bp.route("/community_list", methods=("GET", "POST", "HEAD", "OPTIONS"))
@token.login_required
def community_list():
    if request.method == "POST":
        req_data = request.get_json()
        ppt_id = req_data["property_id"]

        db_conn = get_mysql_db()
        cmnts = db_conn.execute(
            "SELECT id as community_id, community_name, status, address, create_time"
            " FROM mvp.t_community_base "
            " WHERE property_id=?  and is_delete=0"
            " ORDER BY id ASC",
            (ppt_id,)
        ).fetchall()

        cmnts = serialize_row(cmnts)

        return jsonify(code=ReturnCode.SUCCESS.value,
                       data=cmnts)

@api_community_bp.route("/add_community",methods=("GET", "POST", "HEAD", "OPTIONS"))
@token.login_required
def add_community():
    if request.method == "POST":
        req_data = request.get_json()
        ppt_id = req_data["property_id"]
        cmnt_name = req_data["community_name"]
        contact_number = req_data["contact_number"]
        address = req_data["address"]

        err = None
        db_conn = get_mysql_db()

        if (
                db_conn.execute(
                    "SELECT id FROM mvp.t_community_base WHERE community_name = ? and is_delete=0"
                , (cmnt_name,)).fetchone()
                is not None
        ):
            err = "User {0} is already registered.".format(cmnt_name)

        if not err:
            try:
                db_conn.execute(
                    "INSERT INTO mvp.t_community_base "
                    " (community_name, property_id, address, contact_number) "
                    " VALUES (?, ?, ?, ?)",
                    (cmnt_name, ppt_id, address, contact_number)
                )
                db_conn.commit()
            except Exception as ex:
                err = str(ex)

        if err:
            return jsonify(code=ReturnCode.FAIL.value, msg=err)


        return jsonify(code=ReturnCode.SUCCESS.value, msg="")


# 小区资料补充
@api_community_bp.route("/modify_community_info", methods=("GET", "POST", "HEAD", "OPTIONS"))
def modify_community_info():
    return

# 小区资料查询
@api_community_bp.route("/get_community", methods=("GET", "POST", "HEAD", "OPTIONS"))
@token.login_required
def get_community_info():
    if request.method == "POST":
        req_data = request.get_json()
        cmnt_id = req_data["community_id"]

        cmnt = get_community_info_func(cmnt_id)

    return jsonify(code=ReturnCode.SUCCESS.value, data=cmnt)


# 增加楼宇
@api_community_bp.route("/add_community_building",methods=("GET", "POST", "HEAD", "OPTIONS"))
@token.login_required
def add_community_building():
    if request.method == "POST":
        req_data = request.get_json()
        cmnt_id = req_data["community_id"]
        operatior = req_data["member_id"]
        bds = req_data["building"]

        cmnt = get_community_info_func(cmnt_id)
        cmnt_name = cmnt["community_name"]

        db_conn = get_mysql_db()
        db_session_class = sessionmaker(bind=db_conn)
        db_session = db_session_class()

        err = None

        try:
            to_db_data = []
            if isinstance(bds, list):
                for bd in bds:
                    to_db_data.append(
                        {"building_no": bd["building_no"],
                         "building_name": bd["building_name"],
                         "community_id": cmnt_id,
                         "community_name": cmnt_name,
                         "floor_size": bd.get("floor_size"),
                         "create_operatior": operatior}
                    )
            db_session.execute(
                "INSERT INTO t_community_building "
                " (building_no,building_name,community_id,community_name,floor_size,create_operatior)"
                " VALUES (:building_no,:building_name,:community_id,:community_name,:floor_size,:create_operatior)",
                to_db_data
            )
            db_session.commit()
        except Exception as ex:
            err = str(ex)
            db_session.rollback()

        db_session.close()
        if err:
            return jsonify(code=ReturnCode.FAIL.value, msg=err)

    return jsonify(code=ReturnCode.SUCCESS.value, msg="")