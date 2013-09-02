#!/bin/bash
VMCATCHER_EVENT_TYPE="ProcessPrefix"
VMCATCHER_CACHE_DIR_CACHE="/tmp/cache/"
VMCATCHER_EVENT_UUID_SESSION=`uuidgen`
export VMCATCHER_CACHE_DIR_CACHE
export VMCATCHER_EVENT_TYPE
export VMCATCHER_EVENT_UUID_SESSION
export VMCATCHER_EVENT_DC_IDENTIFIER
python vmrecaster -vvv
VMCATCHER_EVENT_TYPE="ExpirePrefix"
VMCATCHER_EVENT_DC_IDENTIFIER="aa42ca85-179b-4873-b12e-32d549bf02b6"
VMCATCHER_EVENT_HV_FORMAT="cpio.bz2"
python vmrecaster -vvv
VMCATCHER_EVENT_TYPE="ExpirePostfix"
python vmrecaster -vvv
VMCATCHER_EVENT_TYPE="AvailablePrefix"
python vmrecaster -vvv
VMCATCHER_EVENT_TYPE="AvailablePostfix"
python vmrecaster -vvv
VMCATCHER_EVENT_TYPE="ProcessPostfix"
VMCATCHER_EVENT_DC_IDENTIFIER=""
VMCATCHER_EVENT_HV_FORMAT=""
python vmrecaster -vvv

echo Finished
