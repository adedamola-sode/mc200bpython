#!/bin/sh

PYIOC=/dls_sw/prod/python3/RHEL7-x86_64/softioc/4.4.0/prefix/bin/pythonSoftIOC

export EPICS_BASE=/dls_sw/spics/R3.14.12.7/base
export EPICS_CA_MAX_ARRAY_BYTES=1000000

cd "$(dirname "$0")"
exec $PYIOC src/BL14I-EA-IOC-38.py "$@"
