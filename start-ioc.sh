#!/bin/sh

cd "$(dirname "$0")"
exec $PYIOC src/BL14I-EA-IOC-38.py "$@"
