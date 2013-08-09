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
        self.Btn_Numerary_1to49 = [QtGui.QPushButton(self)
         for num_draw in xrange(highest_number)]
        button_number = 0
        for button in self.Btn_Numerary_1to49:
            button.setMaximumSize(QtCore.QSize(58, 58))
            button.setAutoFillBackground(True)
            self.gridLayout.addWidget(button,
             int(button_number / 7), int(button_number % 7), 1, 1)
            button_number += 1
            button.setText(str(button_number))

            if button_number in draw_number:
                button.setFlat(False)
                button.setStyleSheet("color: red;")
            else:
                button.setFlat(True)

        self.setWindowTitle(self.tr("Show Drawing"))

        self.boxLayout.addLayout(self.gridLayout)
        self.boxLayout.addWidget(self.buttonBox)

        self.buttonBox.accepted.connect(self.accept)
