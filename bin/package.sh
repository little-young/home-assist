#!/usr/bin/env bash

source /etc/profile
export LANG=en_US.UTF-8

PWD=$(cd `dirname $0`; pwd)
source ${PWD}/env.sh

cd ${PROJ_HOME}/../

exclude="--exclude ${PROJ_NAME}/src --exclude ${PROJ_NAME}/.git --exclude ${PROJ_NAME}/*.tar.* \
         --exclude ${PROJ_NAME}/.idea --exclude ${PROJ_NAME}/*.iml --exclude ${PROJ_NAME}/target"

package_name=${PROJ_NAME}-${VERSION}-${ENV}.tar.gz

tar ${exclude} -czf  ${package_name} ${PROJ_NAME}

echo `currentTime`

ls -lh `pwd`/${package_name}