#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pyLottoSimu

Copyright (C) <2012-2015> Markus Hackspacher

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
import json

try:
    from PyQt5 import QtGui, QtCore, QtWidgets, uic
except ImportError:
    from PyQt4 import QtGui as QtWidgets
    from PyQt4 import QtGui, QtCore, uic

if sys.version_info >= (3, 0):
    unicode = str
else:
    range = xrange


class LottoSettingsDialog(QtWidgets.QDialog):
    """The GUI of Settings. """
    def __init__(self, sysdat, parent=None):
        """Inital user interface and slots
        @return: none
        """
        super(LottoSettingsDialog, self).__init__(parent)

        # Set up the user interface from Designer.
        self.ui = uic.loadUi(os.path.abspath(os.path.join(
                             os.path.dirname(__file__), "lottosystem.ui")))
        self.ui.setWindowIcon(
            QtGui.QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__),
                        "..", "..", "misc", "pyLottoSimu.svg"))))

        self.systemdata = sysdat
        for systemname in self.systemdata.data:
            self.ui.combo_name.addItem(systemname['name'])
        self.ui.combo_name.currentIndexChanged.connect(self.setvalues)
        self.ui.check_with_addit.clicked.connect(self.with_addit)
        self.ui.check_sep_addit_numbers.clicked.connect(self.sep_addit_numbers)

        self.setvalues()

    def init(self):
        """Initial variable
        @return: none
        """
        pass

    def sep_addit_numbers(self):
        check = self.ui.check_sep_addit_numbers.isChecked()
        self.ui.label_max_addit.setEnabled(check)
        self.ui.spinBox_max_addit.setEnabled(check)

    def with_addit(self):
        check = self.ui.check_with_addit.isChecked()
        self.ui.spinBox_addit_numbers.setEnabled(check)
        self.ui.label_addit_numbers.setEnabled(check)
        self.ui.label_sep_addit_numbers.setEnabled(check)
        self.ui.check_sep_addit_numbers.setEnabled(check)
        if check is not True:
            self.ui.check_sep_addit_numbers.setChecked(False)
        self.sep_addit_numbers()

    def setvalues(self):
        """Set Values"""
        index = self.ui.combo_name.currentIndex()
        self.ui.spinBox_max_draw.setValue(
            self.systemdata.data[index]['max_draw'])
        self.ui.spinBox_draw_numbers.setValue(
            self.systemdata.data[index]['draw_numbers'])
        self.ui.check_with_addit.setChecked(
            self.systemdata.data[index]['with_addit'])
        self.ui.spinBox_addit_numbers.setValue(
            self.systemdata.data[index]['addit_numbers'])
        self.ui.check_sep_addit_numbers.setChecked(
            self.systemdata.data[index]['sep_addit_numbers'])
        self.ui.spinBox_max_addit.setValue(
            self.systemdata.data[index]['max_addit'])
        self.with_addit()

    def values(self):
        """Values"""
        return (unicode(self.ui.combo_name.currentText()),
                self.ui.spinBox_max_draw.valueFromText(
                    self.ui.spinBox_max_draw.text()),
                self.ui.spinBox_draw_numbers.valueFromText(
                    self.ui.spinBox_draw_numbers.text()),
                self.ui.check_with_addit.isChecked(),
                self.ui.spinBox_addit_numbers.valueFromText(
                    self.ui.spinBox_addit_numbers.text()),
                self.ui.check_sep_addit_numbers.isChecked(),
                self.ui.spinBox_max_addit.valueFromText(
                    self.ui.spinBox_max_addit.text()))

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getValues(sysdat, parent=None):
        """getValues"""
        dialog = LottoSettingsDialog(sysdat, parent)
        result = dialog.ui.exec_()
        return (dialog.values(), result == QtGui.QDialog.Accepted)


class lottosystemdata():
    def __init__(self, name='Lotto DE', max_draw=49, draw_numbers=6,
                 with_addit=False, addit_numbers=0, sep_addit_numbers=False,
                 max_addit=0):
        self.data = [{
            'name': name,
            'max_draw': max_draw,
            'draw_numbers': draw_numbers,
            'with_addit': with_addit,
            'addit_numbers': addit_numbers,
            'sep_addit_numbers': sep_addit_numbers,
            'max_addit': max_addit},
            {
            'name': 'Lotto AT',
            'max_draw': 45,
            'draw_numbers': 6,
            'with_addit': True,
            'addit_numbers': 1,
            'sep_addit_numbers': False,
            'max_addit': 0},
            {
            'name': 'EuroMillionen',
            'max_draw': 50,
            'draw_numbers': 5,
            'with_addit': True,
            'addit_numbers': 2,
            'sep_addit_numbers': True,
            'max_addit': 11
            }
        ]

    def writetofile(self):
        with open('lottosystems.josn', 'w') as outfile:
            json.dump(self.data, outfile, sort_keys=True,
                      indent=4, separators=(',', ': '))


def gui(arguments, sysdat):
    """Open the GUI of the LottoSettings Dialog
    @param arguments: language, see in folder translate
    @type arguments: string
    @return: none
    """
    if len(arguments) > 1:
        locale = arguments[1]
    else:
        locale = str(QtCore.QLocale.system().name())
        print ("locale: {}".format(locale))
    app = QtWidgets.QApplication([])
    translator = QtCore.QTranslator()
    translator.load(os.path.abspath(os.path.join(os.path.dirname(__file__),
                    "translation", "lotto1_" + locale)))
    app.installTranslator(translator)
    print(LottoSettingsDialog.getValues(sysdat))

if __name__ == "__main__":
    sysdat = lottosystemdata()
    gui('', sysdat)
    sysdat.writetofile()
    # settings = QtCore.QSettings('pylottosimu', 'pylottosimu')

    # settings.setValue('int_value', 42)
    # settings.setValue('point_value', QtCore.QPoint(10, 12))

    # This will write the setting to the platform specific storage.
    # del settings

    # settings = QtCore.QSettings('foo', 'foo')

    # int_value = settings.value('int_value', type=int)
    # print("int_value: %s" % repr(int_value))

    # point_value = settings.value('point_value', type=QtCore.QPoint)
    # print("point_value: %s" % repr(point_value))
