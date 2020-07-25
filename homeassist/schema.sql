
CREATE DATABASE IF NOT EXISTS mvp;

CREATE TABLE IF NOT EXISTS mvp.t_member
(
    id  BIGINT PRIMARY KEY AUTOINCREMENT,
    name  TEXT UNIQUE NOT NULL,
    nick_name  TEXT  DEFAULT '用户',
    password  TEXT  NOT NULL,
    role  INT  NOT NULL DEFAULT 99,
    property_id  INT  NOT NULL,
    create_time  DATETIME,
    update_time  DATETIME,
    is_delete  TINYINT DEFAULT 0,
    EXTEND_JSON TEST
);

CREATE TABLE IF NOT EXISTS mvp.t_property
(
    id  BIGINT PRIMARY KEY AUTOINCREMENT,
    property_name  TEXT UNIQUE NOT NULL,
    contact_name TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT,
    address TEXT,
    create_time  DATETIME,
    update_time  DATETIME,
    is_delete  TINYINT,
    EXTEND_JSON TEST
);

