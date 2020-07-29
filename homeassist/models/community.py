# -*- coding: utf-8 -*-
# @file  : community
# @author: xiaoyang.wang
# @date  : 2020/7/29
import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index, BIGINT
from . import Base

# CREATE TABLE IF NOT EXISTS mvp.t_community_base
# (
#     id  BIGINT PRIMARY KEY AUTOINCREMENT,
#     community_name TEXT UNIQUE NOT NULL,
#     status TINYINT DEFAULT 0,
#     province_id int,
#     city_id int,
#     district_id int,
#     contact_name TEXT NOT NULL,
#     contact_number TEXT NOT NULL,
#     email TEXT,
#     address TEXT,
#     create_time  DATETIME,
#     update_time  DATETIME,
#     is_delete  TINYINT,
#     EXTEND_JSON TEST
# );

class CommumityBase(Base):
    __tablename__ = 't_community_base'                #表名称

    id = Column(Integer, index=True, primary_key=True) # primary_key=True设置主键
    community_name = Column(String(32), nullable=False) #index=True创建索引， nullable=False不为空。
    property_id = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False, default=0)
    province_id = Column(Integer)
    city_id = Column(Integer)
    district_id = Column(Integer)
    address = Column(String(128), nullable=False)
    contact_name = Column(String(32))
    contact_number = Column(String(32), nullable=False)
    email = Column(String(32))
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime)
    extend_json = Column(Text)
    is_delete = Column(Integer, default=0)

    __table_args__ = (
        {"useexisting": True}
    )

    def __repr__(self):
        return '[community {},{}]'.format(self.id, self.community_name)

class CommumityBuilding(Base):
    __tablename__ = 't_community_building'                #表名称

    id = Column(Integer, index=True, primary_key=True) # primary_key=True设置主键
    building_no = Column(Integer, nullable=False)
    building_name = Column(String(32), nullable=False) #index=True创建索引， nullable=False不为空。
    community_id = Column(Integer, nullable=False)
    community_name = Column(String(32), nullable=False)
    floor_size = Column(Integer)
    create_operator = Column(String(32))
    update_operator = Column(String(32))
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime)
    is_delete = Column(Integer, default=0)
    extend_json = Column(Text)

    __table_args__ = (
        {"useexisting": True}
    )
    # community_id 和 building_no唯一

    def __repr__(self):
        return '[community building {},{},{}]'.format(self.id, self.building_no,self.building_name)


class CommunityRoom(Base):
    __tablename__ = 't_community_room'                #表名称

    id = Column(Integer, index=True, primary_key=True) # primary_key=True设置主键
    room_no = Column(Integer, nullable=False)
    room_name = Column(String(32), nullable=False)  # index=True创建索引， nullable=False不为空。
    status = Column(Integer, nullable=False, default=0)
    community_id = Column(Integer, nullable=False)
    community_name = Column(String(32), nullable=False)
    building_no = Column(Integer, nullable=False)
    building_name = Column(String(32), nullable=False)  # index=True创建索引， nullable=False不为空。
    floor = Column(Integer)
    unit = Column(Integer)
    create_operator = Column(String(32))
    update_operator = Column(String(32))
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime)
    is_delete = Column(Integer, default=0)
    extend_json = Column(Text)

    __table_args__ = (
        {"useexisting": True}
    )

    def __repr__(self):
        return '[community room {},{},{}]'.format(self.id, self.room_no, self.room_name)

