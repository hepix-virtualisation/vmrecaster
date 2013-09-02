#!/bin/bash
VMCATCHER_EVENT_TYPE="ProcessPrefix"
VMCATCHER_CACHE_DIR_CACHE="/tmp/cache/"
VMCATCHER_EVENT_UUID_SESSION=`uuidgen`
export VMCATCHER_CACHE_DIR_CACHE
export VMCATCHER_EVENT_TYPE
export VMCATCHER_EVENT_UUID_SESSION
python vmrecaster -vvv
VMCATCHER_EVENT_TYPE="ExpirePrefix"
python vmrecaster -vvv
VMCATCHER_EVENT_TYPE="ExpirePostfix"
python vmrecaster -vvv
VMCATCHER_EVENT_TYPE="AvailablePrefix"
python vmrecaster -vvv
VMCATCHER_EVENT_TYPE="AvailablePostfix"
python vmrecaster -vvv
VMCATCHER_EVENT_TYPE="ProcessPostfix"
python vmrecaster -vvv

echo Finished
