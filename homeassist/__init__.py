# -*- coding: utf-8 -*-
# @file  : __init__.py
# @author: xiaoyang.wang
# @date  : 2020/7/11
import os

from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS

from homeassist import db, config

class FlaskConfig(object):
    JOBS = [
        {
            'trigger': 'interval',
            'seconds': 600,
        }
    ]
    SCHEDULER_API_ENABLED = True
    DB_ENGINE_URL = config.DB_ENGINE_URL
    SECRET_KEY = config.SECRET_KEY


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources=r"/*")
    app.config.from_object(FlaskConfig())

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
        print("app.root:", app.root_path)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import API蓝图
    from homeassist.api.member import api_auth_bp

    # register the database commands & register blueprint
    db.init_app(app)
    app.register_blueprint(api_auth_bp)

    @app.route("/")
    def index():
        # return app.send_static_file('index.html')
        return ""

    @app.route("/healthCheck.jsp")
    def health_check():
        return ""

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="index")

    # 启动定时任务
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    return app

