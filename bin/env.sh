#!/usr/bin/env bash

source /etc/profile
export LANG=en_US.UTF-8

PWD=$(cd `dirname $0`; pwd)

PROJ_HOME=$(cd ${PWD}/../; pwd)
PROJ_LIB=".:${PROJ_HOME}/lib/*"

SCRIPT_DIR="${PROJ_HOME}/scripts/"
BIN_DIR="${PROJ_HOME}/bin/"
CONF_DIR="${PROJ_HOME}/conf"
LOG_DIR="${PROJ_HOME}/logs"


CUR_TIME=$(date +'%Y%m%d-%H%M')

PROJ_NAME=`basename ${PROJ_HOME}`


export DATA_ROOT=/data/prod/homeassist/

export DATABASE="${DATA_ROOT}/homeassist.sqlite"

ENV=dev
VERSION=v1.0.1

if [[ ! -d ${LOG_DIR} ]]; then
    mkdir -p ${LOG_DIR}
fi


function get_day_list() {
    res=""
    day=$2
    start_day=$1
    if [[ ${day} -lt 0 ]]; then
        day=-$2
        start_day=`date -d "$1 $2 day " +%Y-%m-%d`
    fi

    for (( i = 0; i < $day; ++i )); do
        cur=`date -d "$start_day $i day " +%Y-%m-%d`
        res="$res $cur"
    done
    echo ${res}
}


function kill_process() {
    keyword=$1
    threadPidList=$(ps aux | grep ${keyword} | grep -v grep | awk '{print $2}')
    for threadPid in ${threadPidList};
    do
        kill -9 ${threadPid}
        echo "Thread ${threadPid} is killed ok"
    done
}

function currentTime()
{
    echo `date +"%Y-%m-%d %H:%M:%S"`
}


function execute()
{
    t=`currentTime`
    echo "$t START: $1"
    eval $1
    return_val=$?
    t=`currentTime`
    if [[ ${return_val} -eq 0 ]]
    then
        echo "$t SUCCESS: $1"
    else
        echo "$t FAIL: $1"
        exit ${return_val}
    fi
    echo ""
}