# -*- coding: utf-8 -*-

"""
Archerank2

Copyright (C) <2018-2024> Markus Hackspacher

This file is part of pyLottoSimu.

Archerank2 is free software: you can redistribute it and/or modify
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

from PyQt6 import QtGui, QtPrintSupport, QtWidgets


class DlgPrint(QtWidgets.QDialog):
    def __init__(self):
        super(DlgPrint, self).__init__()
        self.setWindowTitle(self.tr('Document Printer'))
        self.setWindowIcon(
            QtGui.QIcon(os.path.abspath(os.path.join(
                os.path.dirname(sys.argv[0]), "misc", "pyLottoSimu.svg"))))
        self.editor = QtWidgets.QTextEdit(self)
        self.editor.textChanged.connect(self.handleTextChanged)
        self.buttonPrint = QtWidgets.QPushButton(self.tr('Print'), self)
        self.buttonPrint.clicked.connect(self.handle_print)
        self.buttonPreview = QtWidgets.QPushButton(self.tr('Preview'), self)
        self.buttonPreview.clicked.connect(self.handle_preview)
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        layout.addWidget(self.buttonPrint, 1, 1)
        layout.addWidget(self.buttonPreview, 1, 2)
        self.handleTextChanged()

    def handle_print(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.editor.document().print_(dialog.printer())

    def handle_preview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.paintRequested.connect(self.editor.print_)
        dialog.exec_()

    def handleTextChanged(self):
        enable = not self.editor.document().isEmpty()
        self.buttonPrint.setEnabled(enable)
        self.buttonPreview.setEnabled(enable)
