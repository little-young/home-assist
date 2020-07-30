#!/usr/bin/env bash
source /etc/profile
export LANG=en_US.UTF-8

PWD=$(cd `dirname $0`; pwd)
source ${PWD}/env.sh


cd ${PROJ_HOME}
python3 -m flask init-db
waitress-serve  --threads=16 --port=80 --call 'homeassist:create_app'
