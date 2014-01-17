#!/bin/bash
pyrcc4 -o lottokugeln_rc.py lottokugeln.qrc
pyrcc4 -o lottokugeln_rc3.py lottokugeln.qrc -py3
echo Hintergrundbild umgewandelt
