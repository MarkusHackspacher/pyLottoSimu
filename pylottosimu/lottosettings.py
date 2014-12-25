#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pyLottoSimu

Copyright (C) <2012-2014> Markus Hackspacher

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
    from PyQt5 import QtGui, QtCore, QtWidgets, uic
    print ("pyQt5")
except ImportError:
    from PyQt4 import QtGui as QtWidgets
    from PyQt4 import QtGui, QtCore, uic
    print ("pyQt4")

if sys.version_info >= (3, 0):
    unicode = str
else:
    range = xrange


class LottoSettingsDialog(QtWidgets.QMainWindow):
    """The GUI of Settings. """
    def __init__(self):
        """Inital user interface and slots
        @return: none
        """
        QtWidgets.QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.ui = uic.loadUi(os.path.abspath(os.path.join(
                             os.path.dirname(__file__), "setting.ui")))
        self.ui.setWindowIcon(
            QtGui.QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__),
                        "..", "misc", "pyLottoSimu.svg"))))


        self.ui.show()

    def init(self):
        """Initial variable
        @return: none
        """

def gui(arguments):
    """Open the GUI
    @param arguments: language (en, de)
    @type arguments: string
    @return: none
    """
    if len(arguments) > 1:
        locale = arguments[1]
    else:
        locale = str(QtCore.QLocale.system().name())
        print ("locale: {}".format(locale))
    app = QtWidgets.QApplication(sys.argv)
    translator = QtCore.QTranslator()
    translator.load(os.path.abspath(os.path.join(os.path.dirname(__file__),
                    "translation", "lotto1_" + locale)))
    app.installTranslator(translator)
    dialog = LottoSettingsDialog()
    sys.exit(app.exec_())

if __name__ == "__main__":
    gui('')
 
