#!/bin/bash
pyuic4 -o lotto.py lotto.ui
echo GUI erstellt
pyrcc4 -o lottokugeln_rc.py lottokugeln.qrc
echo Hintergrundbild umgewandelt