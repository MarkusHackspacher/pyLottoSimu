# -*- coding: utf-8 -*-

"""
pyLottoSimu

Copyright (C) <2012-2013> Markus Hackspacher

This file is part of pyLottoSimu.

pyLottoverwaltung is free software: you can redistribute it and/or modify
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

from os.path import join
from PyQt4 import QtCore, QtGui


class DlgShowDrawing(QtGui.QDialog):
    """Show the numbers in a dialog box"""
    def __init__(self, draw_number, highest_number):
        """
        @param draw_number: the number of draw
        @param highest_number: the number of the PushButtons
        @type draw_number: tuple of int
        @type highest_number: int
        @return: none
        """
        QtGui.QDialog.__init__(self)

        self.setWindowIcon(QtGui.QIcon(join("misc", "icon.ico")))
        self.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)

        self.boxLayout = QtGui.QBoxLayout(QtGui.QBoxLayout.TopToBottom, self)

        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(0)

        #array of Button from 1 to 49
        self.Btn_Numerary_1to49 = []
        for button in xrange(highest_number):
            self.Btn_Numerary_1to49.append(QtGui.QPushButton(self))
            self.Btn_Numerary_1to49[button].setMaximumSize(
             QtCore.QSize(58, 58))
            self.gridLayout.addWidget(self.Btn_Numerary_1to49[button],
             int(button / 7),  int(button % 7), 1, 1)
            self.Btn_Numerary_1to49[button].setAutoFillBackground(True)
            self.Btn_Numerary_1to49[button].setText(str(button + 1))

        for button in xrange(highest_number):
            if button + 1 in draw_number:
                self.Btn_Numerary_1to49[button].setFlat(False)
                self.Btn_Numerary_1to49[button].setStyleSheet("color: red;")
            else:
                self.Btn_Numerary_1to49[button].setFlat(True)

        self.setWindowTitle(self.tr("Show Drawing"))

        self.boxLayout.addLayout(self.gridLayout)
        self.boxLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
