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
    from PyQt5 import QtGui, QtCore, QtWidgets
except ImportError:
    from PyQt4 import QtGui as QtWidgets
    from PyQt4 import QtGui, QtCore
if sys.version_info < (3, 0):
    range = xrange


class DlgShowDrawing(QtWidgets.QDialog):
    """Show the numbers in a dialog box"""
    def __init__(self, draw_number, highest_number):
        """
        @param draw_number: the number of draw
        @param highest_number: the number of the PushButtons
        @type draw_number: tuple of int
        @type highest_number: int
        @return: none
        """
        QtWidgets.QDialog.__init__(self)

        self.setWindowIcon(
            QtGui.QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__),
                        "..", "..", "misc", "pyLottoSimu.svg"))))
        self.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)

        self.boxLayout = QtWidgets.QBoxLayout(
            QtWidgets.QBoxLayout.TopToBottom, self)

        self.gridLayout = QtWidgets.QGridLayout()

        # Array of Button from 1 to 49
        self.Btn_Numerary_1to49 = [QtWidgets.QPushButton(self)
                                   for _ in range(highest_number)]
        for button_number, button in enumerate(self.Btn_Numerary_1to49):
            button.setMaximumSize(QtCore.QSize(58, 58))
            button.setAutoFillBackground(True)
            self.gridLayout.addWidget(
                button, int(button_number / 7), int(button_number % 7), 1, 1)
            button.setText(str(button_number + 1))

            if button_number in draw_number:
                button.setFlat(False)
                button.setStyleSheet("color: red;")
            else:
                button.setFlat(True)

        self.setWindowTitle(self.tr("Show Drawing"))

        self.boxLayout.addLayout(self.gridLayout)
        self.boxLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
