#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
pyLottoSimu, load module lotto

Copyright (C) <2012-2024> Markus Hackspacher

This file is part of pyLottoSimu.

pyLottoSimu is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyLottoSimu is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyLottoSimu.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys

try:
    from PyQt6 import QtCore, QtWidgets
except ImportError:
    from PyQt5 import QtCore, QtWidgets

from pylottosimu import pylotto


def gui(arguments):
    """Open the GUI

    :param arguments: language, see in folder translate
    :type arguments: string
    :returns: none
    """
    if len(arguments) > 1:
        locale = arguments[1]
    else:
        locale = str(QtCore.QLocale.system().name())
        print("locale: {}".format(locale))
    app = QtWidgets.QApplication(sys.argv)
    translator = QtCore.QTranslator()
    translator.load(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]),
                    "pylottosimu", "translation", "lotto1.{}".format(locale))))
    app.installTranslator(translator)
    dialog = pylotto.LottoSimuDialog()
    sys.exit(app.exec())


gui(sys.argv)
