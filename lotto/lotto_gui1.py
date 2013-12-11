#!/usr/bin/env python
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
__doc__ = "The signals for the GUI"

import sys
import time
import webbrowser
from datetime import datetime
from random import randint
from os.path import join
from PyQt4 import QtGui, QtCore, uic

import lotto.lottokugeln_rc
from lotto.dialog.show_drawing import DlgShowDrawing
from lotto.zufallszahl import zufallszahlen


class MeinDialog(QtGui.QMainWindow):
    """The GUI and programm of the pyLottoSimu. """
    def __init__(self):
        """Inital user interface and slots
        @return: none
        """
        QtGui.QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.ui = uic.loadUi(join("lotto", "lotto.ui"))
        self.ui.setWindowIcon(QtGui.QIcon(join("misc", "pyLottoSimu.svg")))

        self.action_lottosim()
        self.timer = QtCore.QTimer(self)

        # Slots
        self.ui.btn_random_numbers.clicked.connect(
         self.onrandom_numbers_generator)
        self.ui.clean_output_text.clicked.connect(self.onclean_output_text)
        self.ui.btn_start.clicked.connect(self.onbtn_start)
        self.ui.actionBeenden.triggered.connect(self.onclose)
        self.ui.actionInfo.triggered.connect(self.oninfo)
        self.ui.actionGo_to_the_website.triggered.connect(self.onwebsite)
        self.ui.actionLottosimulation.changed.connect(self.action_lottosim)
        self.ui.btn_draw_overview.clicked.connect(self.onbtn_draw_overview)
        self.timer.timeout.connect(self.ontimer)
        self.ui.statusBar().showMessage(self.tr('ready'))

        self.ui.show()

    def init(self):
        """Inital variable
        @return: none
        """
        self.turn = 0
        self.i_hochste = int(self.ui.sbox_from_a_set_of.text())
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
            self.ui.label_zahl.setText(str(zufallszahlen(1,
             int(self.ui.sbox_from_a_set_of.text()))[0]))
        self.timer.start(100)
        if self.delay_of_next_number < 0:
            self.show_next_number()
            self.delay_of_next_number = verz

    def show_next_number(self):
        """Simulation of the draw and show the next Number on the Screen.  
        @return: none
        """
        self.ui.label_zahl_2.setText(str(self.random_number[self.turn]))
        self.ui.label_zahl.setText(str(self.random_number[self.turn]))
        if self.turn == (len(self.random_number) - 2):
            text = self.tr('Now we come to the number {0}, and thus '
             'the penultimate number of todays draw. It is the {1}.')
            text = unicode(text).format(self.zaehlzahlen[self.turn],
              self.random_number[self.turn])
        elif self.turn == (len(self.random_number) - 1):
            text = self.tr('And now we come to the {0} and last'
             'winning number, it is the {1}.')
            text = unicode(text).format(self.zaehlzahlen[self.turn],
              self.random_number[self.turn])
            self.ui.plainTextEdit.appendPlainText(text)
            random_number = sorted(self.random_number[:])
            text1 = "".join(map(" {0:02d}".format, random_number))
            text = self.tr('That was todays lottery draw, '
            'the figures were:{0}, '
            'I wish you a nice evening! Bye, bye!')
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
                Textnumber = randint(0, len(self.textauswahl) - 1)
                if Textnumber != self.LastTextnumber:
                    break
            text = self.textauswahl[Textnumber].format(
             self.zaehlzahlen[self.turn],
             self.random_number[self.turn])
            self.LastTextnumber = Textnumber
        self.ui.plainTextEdit.appendPlainText(text)
        self.turn += 1

    def onbtn_draw_overview(self):
        """show dialog of the draw"""
        dlgdraw = DlgShowDrawing(self.random_number, self.i_hochste)
        dlgdraw.exec_()
 
    def onbtn_start(self):
        """Start simulation with the first drawing
        init timer with the valve from the Scrollbar
        the next drawing starts with the timer event.
        @return: none
        """
        self.ui.plainTextEdit.setPlainText("")
        self.ui.label_zahl_2.setText("")
        self.turn = 0
        dt = datetime.now()
        i_anzahl = int(self.ui.sbox_drawn_numbers.text())
        self.i_hochste = int(self.ui.sbox_from_a_set_of.text())
        self.random_number = zufallszahlen(i_anzahl, self.i_hochste)
        text = self.tr('Welcome to the lottery draw,\n'
         'at {0}.\nnumbers are drawn: {1} out of {2}!')
        text = unicode(text).format(
         dt.strftime("%d %B %Y um %H:%M"), i_anzahl, self.i_hochste)
        self.ui.plainTextEdit.appendPlainText(text)
        self.timer.start(100)
        self.delay_of_next_number = self.ui.horizontalSlider.value()
        textauswahl_tr = [
            self.tr(
            'And now we come to the winning number {0}, it is the {1}.'),
            self.tr(
            "The {0} lotto number of today's draw is the {1}."),
            self.tr(
            'Now we come to winning number {0}, this is the {1}.',),
            self.tr(
            "Now we come to {0} number of today's draw ... {1}.",),
            self.tr('The {0} winning number is {1}.')]
        self.textauswahl = map(unicode, textauswahl_tr)
        zaehlzahlen_tr = [self.tr('first'), self.tr('second'),
         self.tr('third'), self.tr('fourth'), self.tr('fifth'),
         self.tr('sixth'), self.tr('seventh'), self.tr('eighth'),
         self.tr('ninth'), self.tr('10th'), self.tr('11th'),
         self.tr('12th'), self.tr('13th'), self.tr('14th'),
         self.tr('15th')]
        self.zaehlzahlen = map(unicode, zaehlzahlen_tr)

    def action_lottosim(self):
        """Changing the layout for simulation or generation
        Move the textedit and change the visible.
        @return: none
        """
        self.ui.plainTextEdit.setPlainText("")
        if self.ui.actionLottosimulation.isChecked():
            # lotto simulation
            self.ui.statusBar().showMessage(self.tr('lotto simulation'))
            self.ui.plainTextEdit.setGeometry(QtCore.QRect(20, 180, 441, 136))
            self.ui.btn_random_numbers.setVisible(False)
            self.ui.clean_output_text.setVisible(False)
            self.ui.label_Lottozahlen.setVisible(False)
            self.ui.label_zahl.setVisible(True)
            self.ui.label_zahl_2.setVisible(True)
            self.ui.label_Geschwindigkeit.setVisible(True)
            self.ui.label_zahl.setText("")
            self.ui.label_zahl_2.setText("")
            self.ui.btn_start.setVisible(True)
            self.ui.horizontalSlider.setVisible(True)
            self.ui.btn_draw_overview.setVisible(False)
            self.ui.rdbtn_show_draw_after.setVisible(True)

        else:
            #random numbers
            self.ui.statusBar().showMessage(self.tr('random numbers'))
            self.ui.plainTextEdit.setGeometry(QtCore.QRect(20, 20, 441, 111))
            self.ui.btn_random_numbers.setVisible(True)
            self.ui.clean_output_text.setVisible(True)
            self.ui.label_Lottozahlen.setVisible(True)
            self.ui.label_zahl.setVisible(False)
            self.ui.label_zahl_2.setVisible(False)
            self.ui.label_Geschwindigkeit.setVisible(False)
            self.ui.btn_start.setVisible(False)
            self.ui.horizontalSlider.setVisible(False)
            self.ui.btn_draw_overview.setVisible(False)
            self.ui.rdbtn_show_draw_after.setVisible(False)
            self.timer.stop()

    def onrandom_numbers_generator(self):
        """Show the output from the random number generator.  
        @return: none
        """
        i_anzahl = int(self.ui.sbox_drawn_numbers.text())
        i_hochste = int(self.ui.sbox_from_a_set_of.text())
        random_numbers = sorted(zufallszahlen(i_anzahl, i_hochste))
        if random_numbers:
            text = "".join(map(" {0:02d}".format, random_numbers))
        else:
            text = self.tr("Error, no valid numbers available!")
        dt = datetime.now()
        text = dt.strftime("%H:%M:%S: ") + str(i_anzahl) + \
         self.tr(" out of ") + str(i_hochste) + ": " + text
        self.ui.plainTextEdit.appendPlainText(text)

    def onclean_output_text(self):
        """Clean the output text
        @return: none"""
        self.ui.plainTextEdit.setPlainText("")

    def oninfo(self):
        """Infoscreen
        @return: none"""
        text = self.tr(
        'simulation of a random draw\n\n'
        'based on an idea of imageupload,\n'
        'http://www.my-image-upload.de/\n\n'
        'Lizenz: GNU GPL v3\n'
        'http://www.gnu.org/licenses/')
        a = QtGui.QMessageBox()
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
        webbrowser.open_new_tab("http://markush.cwsurf.de/"
         "joomla_17/index.php/python/pylottosimu/")

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
        locale = unicode(QtCore.QLocale.system().name())
        print ("locale: " + locale)
    app = QtGui.QApplication(sys.argv)
    translator = QtCore.QTranslator()
    translator.load(join("lotto", "translation", "lotto1_" + locale))
    app.installTranslator(translator)
    dialog = MeinDialog()
    sys.exit(app.exec_())

if __name__ == "__main__":
    gui()
