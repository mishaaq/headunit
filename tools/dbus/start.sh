#!/bin/sh

dbus-launch --config-file=hmi.conf
python nativeguictrl_stub.py