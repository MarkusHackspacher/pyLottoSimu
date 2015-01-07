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
__doc__ = "The signals for the GUI"

import os
import sys
import webbrowser
from datetime import datetime
from random import randint
import random

try:
    from PyQt5 import QtGui, QtCore, QtWidgets, uic
    print ("pyQt5")
except ImportError:
    from PyQt4 import QtGui as QtWidgets
    from PyQt4 import QtGui, QtCore, uic
    print ("pyQt4")

if sys.version_info >= (3, 0):
    if QtCore.QT_VERSION >= 0x050000:
        import pylottosimu.lottokugeln_rc3_qt5 as lottokugeln_rc
    else:
        import pylottosimu.lottokugeln_rc3 as lottokugeln_rc
    from pylottosimu.dialog.show_drawing import DlgShowDrawing
    import pylottosimu.dialog.lottosystem as DlgLottoSystem
    unicode = str
else:
    import lottokugeln_rc as lottokugeln_rc
    from dialog.show_drawing import DlgShowDrawing
    import dialog.lottosystem as DlgLottoSystem
range = xrange


class LottoSimuDialog(QtWidgets.QMainWindow):
    """The GUI and programm of the pyLottoSimu. """
    def __init__(self):
        """Inital user interface and slots
        @return: none
        """
        QtWidgets.QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.ui = uic.loadUi(os.path.abspath(os.path.join(
                             os.path.dirname(__file__), "lottosimu_gui.ui")))
        self.ui.setWindowIcon(
            QtGui.QIcon(os.path.abspath(os.path.join(os.path.dirname(__file__),
                        "..", "misc", "pyLottoSimu.svg"))))

        self.action_lottosim()
        self.timer = QtCore.QTimer(self)

        # Slots
        self.ui.btn_random_numbers.clicked.connect(
            self.onrandom_numbers_generator)
        self.ui.clean_output_text.clicked.connect(self.onclean_output_text)
        self.ui.btn_start.clicked.connect(self.onbtn_start)
        self.ui.action_quit.triggered.connect(self.onclose)
        self.ui.action_info.triggered.connect(self.oninfo)
        self.ui.action_go_to_the_website.triggered.connect(self.onwebsite)
        self.ui.action_lotto_simulation.changed.connect(self.action_lottosim)
        self.ui.btn_draw_overview.clicked.connect(self.onbtn_draw_overview)
        self.timer.timeout.connect(self.ontimer)
        self.ui.statusBar().showMessage(self.tr('ready'))
        self.ui.actionLotto_system.triggered.connect(self.onsystem)

        self.ui.show()

    def init(self):
        """Initial variable
        @return: none
        """
        self.turn = 0
        self.highest = int(self.ui.sbox_from_a_set_of.text())
        self.random_number = 0
        self.delay_of_next_number = self.ui.horizontalSlider.value()

    def ontimer(self):
        """Start time to show a number.
        @return: none
        """
        self.timer.stop()
        verz = self.ui.horizontalSlider.value()
        if self.delay_of_next_number >= verz:
            self.delay_of_next_number = verz
        self.delay_of_next_number -= 1
        if self.delay_of_next_number < 10 \
                or (self.delay_of_next_number < 17
                    and (self.delay_of_next_number % 2) == 0) \
                or (self.delay_of_next_number < 25
                    and (self.delay_of_next_number % 3) == 0) \
                or (self.delay_of_next_number % 4) == 0:
            self.ui.label_big_number.setText(str(
                random.sample(range(1, int(
                    self.ui.sbox_from_a_set_of.text()) + 1), 1)[0]))
        self.timer.start(100)
        if self.delay_of_next_number < 0:
            self.show_next_number()
            self.delay_of_next_number = verz

    def show_next_number(self):
        """Simulation of the draw and show the next Number on the Screen.
        @return: none
        """
        self.ui.label_last_draw_number.setText(
            str(self.random_number[self.turn]))
        self.ui.label_big_number.setText(str(self.random_number[self.turn]))
        if self.turn == (len(self.random_number) - 2):
            text = self.tr("Now we come to the number {0}, and thus the "
                           "penultimate number of today's draw. It is the {1}.")
            text = unicode(text).format(self.countnumbers[self.turn],
                                        self.random_number[self.turn])
        elif self.turn == (len(self.random_number) - 1):
            text = self.tr('And now we come to the {0} and last'
                           'winning number, it is the {1}.')
            text = unicode(text).format(self.countnumbers[self.turn],
                                        self.random_number[self.turn])
            self.ui.plaintextedit.appendPlainText(text)
            random_number = sorted(self.random_number[:])
            text1 = "".join(map(" {0:02d}".format, random_number))
            text = self.tr("That was today's lottery draw, "
                           "the figures were:{0}, "
                           "I wish you a nice evening! Bye, bye!")
            text = unicode(text).format(text1)
            self.timer.stop()
            if self.ui.rdbtn_show_draw_after.isChecked():
                self.onbtn_draw_overview()
            self.ui.btn_draw_overview.setVisible(True)
        elif self.turn >= len(self.random_number):
            self.timer.stop()
            text = ''
        elif self.turn == 0:
            self.ui.btn_draw_overview.setVisible(False)
            text = self.tr('And the first winning number is the {0}.')
            text = unicode(text).format(self.random_number[self.turn])
            self.LastTextnumber = -1
        else:
            while True:
                Textnumber = randint(0, len(self.textselection) - 1)
                if Textnumber != self.LastTextnumber:
                    break
            text = self.textselection[Textnumber].format(
                self.countnumbers[self.turn],
                self.random_number[self.turn])
            self.LastTextnumber = Textnumber
        self.ui.plaintextedit.appendPlainText(text)
        self.turn += 1

    def onbtn_draw_overview(self):
        """show dialog of the draw"""
        dlgdraw = DlgShowDrawing(self.random_number, self.highest)
        dlgdraw.exec_()

    def onsystem(self):
        """show dialog of the draw"""
        sysdat = DlgLottoSystem.lottosystemdata()
        system = DlgLottoSystem.LottoSettingsDialog.getValues(sysdat)
        if system[1]:
            self.ui.sbox_drawn_numbers.setValue(system[0][2])
            self.ui.sbox_from_a_set_of.setValue(system[0][1])

    def onbtn_start(self):
        """Start simulation with the first drawing
        init timer with the valve from the Scrollbar
        the next drawing starts with the timer event.
        @return: none
        """
        self.ui.plaintextedit.setPlainText("")
        self.ui.label_last_draw_number.setText("")
        self.turn = 0
        dt = datetime.now()
        drawn_numbers = int(self.ui.sbox_drawn_numbers.text())
        self.highest = int(self.ui.sbox_from_a_set_of.text())
        self.random_number = \
            random.sample(range(1, self.highest + 1), drawn_numbers)
        text = self.tr('Welcome to the lottery draw,\n'
                       'at {0}.\nnumbers are drawn: {1} out of {2}!')
        text = unicode(text).format(
            dt.strftime("%d %B %Y um %H:%M"), drawn_numbers, self.highest)
        self.ui.plaintextedit.appendPlainText(text)
        self.timer.start(100)
        self.delay_of_next_number = self.ui.horizontalSlider.value()
        textselection_tr = [
            self.tr(
                "And now we come to the winning number {0}, it is the {1}."),
            self.tr(
                "The {0} lotto number of today's draw is the {1}."),
            self.tr(
                "Now we come to winning number {0}, this is the {1}.",),
            self.tr(
                "Now we come to {0} number of today's draw ... {1}.",),
            self.tr('The {0} winning number is {1}.')]
        countnumbers_tr = [self.tr('first'), self.tr('second'),
                           self.tr('third'), self.tr('fourth'),
                           self.tr('fifth'), self.tr('sixth'),
                           self.tr('seventh'), self.tr('eighth'),
                           self.tr('ninth'), self.tr('10th'),
                           self.tr('11th'), self.tr('12th'),
                           self.tr('13th'), self.tr('14th'),
                           self.tr('15th')]
        if sys.version_info >= (3, 0):
            self.textselection = textselection_tr
            self.countnumbers = countnumbers_tr
        else:
            self.textselection = map(unicode, textselection_tr)
            self.countnumbers = map(unicode, countnumbers_tr)

    def action_lottosim(self):
        """Changing the layout for simulation or generation
        Move the textedit and change the visible.
        @return: none
        """
        self.ui.plaintextedit.setPlainText("")
        if self.ui.action_lotto_simulation.isChecked():
            # lotto simulation
            self.ui.statusBar().showMessage(self.tr('lotto simulation'))
            self.ui.plaintextedit.setGeometry(QtCore.QRect(20, 180, 441, 136))
            self.ui.btn_random_numbers.setVisible(False)
            self.ui.clean_output_text.setVisible(False)
            self.ui.label_Lottozahlen.setVisible(False)
            self.ui.label_big_number.setVisible(True)
            self.ui.label_last_draw_number.setVisible(True)
            self.ui.label_speed.setVisible(True)
            self.ui.label_big_number.setText("")
            self.ui.label_last_draw_number.setText("")
            self.ui.btn_start.setVisible(True)
            self.ui.horizontalSlider.setVisible(True)
            self.ui.btn_draw_overview.setVisible(False)
            self.ui.rdbtn_show_draw_after.setVisible(True)

        else:
            # random numbers
            self.ui.statusBar().showMessage(self.tr('random numbers'))
            self.ui.plaintextedit.setGeometry(QtCore.QRect(20, 20, 441, 111))
            self.ui.btn_random_numbers.setVisible(True)
            self.ui.clean_output_text.setVisible(True)
            self.ui.label_Lottozahlen.setVisible(True)
            self.ui.label_big_number.setVisible(False)
            self.ui.label_last_draw_number.setVisible(False)
            self.ui.label_speed.setVisible(False)
            self.ui.btn_start.setVisible(False)
            self.ui.horizontalSlider.setVisible(False)
            self.ui.btn_draw_overview.setVisible(False)
            self.ui.rdbtn_show_draw_after.setVisible(False)
            self.timer.stop()

    def onrandom_numbers_generator(self):
        """Show the output from the random number generator.
        @return: none
        """
        drawn_numbers = int(self.ui.sbox_drawn_numbers.text())
        highest = int(self.ui.sbox_from_a_set_of.text())
        random_numbers = sorted(
            random.sample(range(1, highest + 1), drawn_numbers))
        if random_numbers:
            text = "".join(map(" {0:02d}".format, random_numbers))
        else:
            text = self.tr("Error, no valid numbers available!")
        dt = datetime.now()
        text = dt.strftime("%H:%M:%S: ") + str(drawn_numbers) + \
            self.tr(" out of ") + str(highest) + ": " + text
        self.ui.plaintextedit.appendPlainText(text)

    def onclean_output_text(self):
        """Clean the output text
        @return: none"""
        self.ui.plaintextedit.setPlainText("")

    def oninfo(self):
        """info message box
        @return: none"""
        text = self.tr(
            'simulation of a random draw\n\n'
            'based on an idea of imageupload,\n'
            'http://www.my-image-upload.de/\n\n'
            'GNU GPL v3\n'
            'http://www.gnu.org/licenses/')
        a = QtWidgets.QMessageBox()
        a.setWindowTitle(self.tr('Info'))
        a.setText(text)
        text = self.tr('Created with Python by Markus Hackspacher '
                       'http://markush.cwsurf.de')
        a.setInformativeText(text)
        a.exec_()

    def onwebsite(self):
        """Open website
        @return: none
        """
        webbrowser.open_new_tab(
            "http://markush.cwsurf.de/joomla_17/index.php/python/pylottosimu/")

    def onclose(self):
        """Close the GUI
        @return: none"""
        self.ui.close()


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
    dialog = LottoSimuDialog()
    sys.exit(app.exec_())

if __name__ == "__main__":
    gui('')
