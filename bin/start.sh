#!/usr/bin/env bash

source /etc/profile
export LANG=en_US.UTF-8

PWD=$(cd `dirname $0`; pwd)
source ${PWD}/env.sh


cd ${PROJ_HOME}
export FLASK_APP=homeassist
export FLASK_ENV=production
#export FLASK_ENV=development

PID=$(ps -ef | grep ${FLASK_APP}|grep waitress-serve| grep -v grep | awk '{print $2}')
if [ -z "$PID" ] ;then
    echo "start ${FLASK_APP}"
    nohup sh ${BIN_DIR}/service.sh 1>>${LOG_DIR}/chandler.log 2>&1 &
else
    echo "${FLASK_APP} already running"
fi