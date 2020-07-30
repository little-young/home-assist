
CREATE DATABASE IF NOT EXISTS mvp;

CREATE TABLE IF NOT EXISTS mvp.t_member
(
    id  BIGINT PRIMARY KEY AUTO_INCREMENT,
    name  TEXT UNIQUE NOT NULL,
    nick_name  TEXT  DEFAULT '用户',
    password  TEXT  NOT NULL,
    role  INT  NOT NULL DEFAULT 99,
    property_id  INT  NOT NULL,
    create_time  DATETIME,
    update_time  DATETIME,
    is_delete  TINYINT DEFAULT 0,
    EXTEND_JSON TEXT
);

CREATE TABLE IF NOT EXISTS mvp.t_property
(
    id  BIGINT PRIMARY KEY AUTOINCREMENT,
    property_name  TEXT UNIQUE NOT NULL,
    legal_person  TEXT NOT NULL,
    license_no    TEXT NOT NULL,
    property_level  INTEGER NOT NULL DEFAULT 0,
    contact_name TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT,
    address TEXT,
    create_time  DATETIME,
    update_time  DATETIME,
    is_delete  TINYINT,
    EXTEND_JSON TEXT
);

CREATE TABLE IF NOT EXISTS mvp.t_community_base
(
    id  BIGINT PRIMARY KEY AUTOINCREMENT,
    community_name TEXT UNIQUE NOT NULL,
    property_id BIGINT UNIQUE NOT NULL,
    status TINYINT DEFAULT 0,
    province_id int,
    city_id int,
    district_id int,
    address TEXT,
    contact_name TEXT NOT NULL,
    contact_number TEXT NOT NULL,
    email TEXT,
    create_time  DATETIME,
    update_time  DATETIME,
    is_delete  TINYINT,
    EXTEND_JSON TEXT
);

--CREATE TABLE IF NOT EXISTS mvp.t_community_info
--(
--    id  BIGINT PRIMARY KEY AUTOINCREMENT,
--    community_id BIGINT PRIMARY KEY UNIQUE NOT NULL,
--    community_name TEXT UNIQUE NOT NULL,
--    create_time  DATETIME,
--    update_time  DATETIME,
--    is_delete  TINYINT,
--    EXTEND_JSON TEXT
--);
CREATE TABLE IF NOT EXISTS mvp.t_community_building
(
    id  BIGINT PRIMARY KEY AUTOINCREMENT,
    building_no INT NOT NULL,
    building_name TEXT NOT NULL,
    community_id BIGINT NOT NULL,
    community_name TEXT UNIQUE NOT NULL,
    floor_size INT,
    create_operator TEXT,
    update_operator TEXT,
    create_time  DATETIME,
    update_time  DATETIME,
    is_delete  TINYINT,
    EXTEND_JSON TEXT
);

--CREATE TABLE IF NOT EXISTS mvp.t_community_unit
--(
--    id  BIGINT PRIMARY KEY AUTOINCREMENT,
--    community_id BIGINT PRIMARY KEY UNIQUE NOT NULL,
--);

CREATE TABLE IF NOT EXISTS mvp.t_community_room
(
    id  BIGINT PRIMARY KEY AUTOINCREMENT,
    room_no INT NOT NULL,
    room_name TEXT NOT NULL,
    status TINYINT NOT NULL DEFAULT 0,
    community_id BIGINT NOT NULL,
    community_name TEXT NOT NULL,
    building_no BIGINT NOT NULL,
    building_name TEXT NOT NULL,
    floor INT,
    unit INT,
    space_size INT COMMMENT '单位:平米',
    create_operator TEXT,
    update_operator TEXT,
    create_time  DATETIME,
    update_time  DATETIME,
    is_delete  TINYINT,
    EXTEND_JSON TEXT
);
