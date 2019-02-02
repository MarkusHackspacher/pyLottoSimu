#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyLottoSimu

# Copyright (C) <2012-2018> Markus Hackspacher

# This file is part of pyLottoSimu.

# pyLottoSimu is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pyLottoSimu is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pyLottoSimu.  If not, see <http://www.gnu.org/licenses/>.

"""class LottoSimuDialog
---------------------

Load the GUI and manage the signals for the program of the pyLottoSimu.
Use the lottosimu_gui.ui

class drawlotto
---------------

simulate a lotto draw.
draw the lotto numbers and give the draw text back
"""

import os
import random
import sys
import webbrowser
from datetime import datetime
from random import randint

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtSvg import QSvgWidget

from pylottosimu.dialog.lottosettingdialog import LottoSettingsDialog
from pylottosimu.dialog.show_drawing import DlgShowDrawing
from pylottosimu.lottosystem import LottoSystemData


class LottoSimuDialog(QtWidgets.QMainWindow):
    """The GUI and program of the pyLottoSimu.
    """
    def __init__(self):
        """Initial user interface and slots

        :returns: none
        """
        super(LottoSimuDialog, self).__init__()

        # Set up the user interface from Designer.
        try:
            self.ui = uic.loadUi(os.path.join(
                "pylottosimu", "lottosimu_gui.ui"))
        except FileNotFoundError:
            self.ui = uic.loadUi(os.path.abspath(os.path.join(
                os.path.dirname(sys.argv[0]),
                "pylottosimu", "lottosimu_gui.ui")))
        self.ui.setWindowIcon(
            QtGui.QIcon(os.path.abspath(os.path.join(
                os.path.dirname(sys.argv[0]), "misc", "pyLottoSimu.svg"))))

        self.imageLabel = QSvgWidget()
        self.imageLabel.renderer().load(os.path.abspath(os.path.join(
            os.path.dirname(sys.argv[0]),
            "pylottosimu", "lottokugel.svg")))
        self.ui.scrollArea.setWidget(self.imageLabel)

        self.actionLottoSim()
        self.timer = QtCore.QTimer(self)
        self.sysdat = LottoSystemData()

        # Slots
        self.ui.btn_random_numbers.clicked.connect(
            self.randomNumbersGenerator)
        self.ui.clean_output_text.clicked.connect(self.cleanOutputText)
        self.ui.btn_start.clicked.connect(self.onBtnStart)
        self.ui.action_quit.triggered.connect(self.onClose)
        self.ui.action_info.triggered.connect(self.onInfo)
        self.ui.action_go_to_the_website.triggered.connect(self.openWebsite)
        self.ui.action_lotto_simulation.changed.connect(self.actionLottoSim)
        self.ui.btn_draw_overview.clicked.connect(self.onDrawOverview)
        self.timer.timeout.connect(self.onTimer)
        self.ui.statusBar().showMessage(self.tr('ready'))
        self.ui.actionLotto_system.triggered.connect(self.onSystem)

        self.turn = 0
        self.random_number = 0
        self.delay_of_next_number = self.ui.horizontalSlider.value()
        self.lottodraw = DrawLotto()
        self.ui.label_numbers.setText(self.lottodraw.data['name'])
        self.ui.show()

    def onTimer(self):
        """Start time to show a number.

        :returns: none
        """
        self.timer.stop()
        verz = self.ui.horizontalSlider.value()
        if self.delay_of_next_number >= verz:
            self.delay_of_next_number = verz
        self.delay_of_next_number -= 1
        if (self.delay_of_next_number < 10 or
                (self.delay_of_next_number < 17 and
                    (self.delay_of_next_number % 2) == 0) or
                (self.delay_of_next_number < 25 and
                    (self.delay_of_next_number % 3) == 0) or
                (self.delay_of_next_number % 4) == 0):
            self.ui.label_big_number.setText(str(
                random.sample(range(1, int(
                    self.lottodraw.data['max_draw']) + 1), 1)[0]))
        self.timer.start(100)
        if self.delay_of_next_number < 0:
            self.showNextNumber()
            self.delay_of_next_number = verz

    def showNextNumber(self):
        """Simulation of the draw and show the next Number on the Screen.

        :returns: none
        """
        if self.turn == 0:
            self.ui.btn_draw_overview.setVisible(False)

        if self.turn >= len((self.lottodraw.random_number +
                             self.lottodraw.random_addit)):
            self.timer.stop()
            if self.ui.rdbtn_show_draw_after.isChecked():
                self.onDrawOverview()
            self.ui.btn_draw_overview.setVisible(True)
        else:
            self.ui.label_last_draw_number.setText(str((
                self.lottodraw.random_number +
                self.lottodraw.random_addit)[self.turn]))
            self.ui.label_big_number.setText(str((
                self.lottodraw.random_number +
                self.lottodraw.random_addit)[self.turn]))

        self.ui.plaintextedit.appendPlainText(self.lottodraw.picknumber(
            self.turn))

        self.turn += 1

    def onDrawOverview(self):
        """show dialog of the draw

        :returns: none
        """
        separetebonus = False
        if self.lottodraw.data['sep_addit_numbers']:
            separetebonus = self.lottodraw.data['max_addit']

        dlgdraw = DlgShowDrawing(self.lottodraw.ballnumber,
                                 self.lottodraw.data['max_draw'],
                                 self.lottodraw.ballbonus,
                                 highestbonus=separetebonus
                                 )
        dlgdraw.exec_()

    def onSystem(self):
        """show dialog of the draw

        :returns: none
        """
        system = LottoSettingsDialog.get_values(self.sysdat)

        if system[1]:
            self.lottodraw.data['name'] = system[0][0]
            self.lottodraw.data['max_draw'] = system[0][1]
            self.lottodraw.data['draw_numbers'] = system[0][2]
            self.lottodraw.data['with_addit'] = system[0][3]
            self.lottodraw.data['addit_numbers'] = system[0][4]
            self.lottodraw.data['sep_addit_numbers'] = system[0][5]
            self.lottodraw.data['max_addit'] = system[0][6]
            self.lottodraw.data['name_addition'] = system[0][7]

        self.ui.label_numbers.setText(self.lottodraw.data['name'])
        self.ui.btn_draw_overview.setVisible(False)

    def onBtnStart(self):
        """Start simulation with the first drawing
        init timer with the valve from the Scrollbar
        the next drawing starts with the timer event.

        :returns: none
        """
        self.ui.label_last_draw_number.setText("")
        self.turn = 0
        self.lottodraw.draw()
        self.ui.plaintextedit.setPlainText(self.lottodraw.picknumber(-1))
        self.timer.start(100)
        self.delay_of_next_number = self.ui.horizontalSlider.value()

    def actionLottoSim(self):
        """Changing the layout for simulation or generation
        and change the visible of the buttons.

        :returns: none
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

    def randomNumbersGenerator(self):
        """Show the output from the random number generator.

        :returns: none
        """
        self.lottodraw.draw()
        if self.lottodraw.random_number:
            text = "".join(map(" {0:02d}".format, sorted(
                self.lottodraw.random_number)))
        else:
            text = self.tr("Error, no valid numbers available!")
        dt = datetime.now()
        texttr = self.tr("{}: {} out of {}: {}")
        text = str(texttr).format(dt.strftime("%H:%M:%S"),
                                  self.lottodraw.data['draw_numbers'],
                                  self.lottodraw.data['max_draw'], text)
        self.ui.plaintextedit.appendPlainText(text)

    def cleanOutputText(self):
        """Clean the output text

        :returns: none
        """
        self.ui.plaintextedit.setPlainText("")

    def onInfo(self, test=None):
        """Set the text for the info message box in html format

        :returns: none
        """
        infobox = QtWidgets.QMessageBox()
        infobox.setWindowTitle(self.tr('Info'))
        infobox.setText(self.tr(
            'The simulation of a lottery draw based on an idea of '
            '<a href="http://www.m-i-u.de/">my-image-upload.de</a>,<br><br>'
            'pyLottoSimu is free software and use GNU General Public License '
            '<a href="http://www.gnu.org/licenses/">www.gnu.org/licenses</a>'))
        infobox.setInformativeText(self.tr(
            'More Information about the program at '
            '<a href="http://pylottosimu.readthedocs.io">'
            'pylottosimu.readthedocs.io</a>'))
        if test:
            infobox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            button = infobox.button(QtWidgets.QMessageBox.Ok)
            QtCore.QTimer.singleShot(0, button.clicked)
        infobox.exec_()

    @staticmethod
    def openWebsite():
        """Open website

        :returns: none
        """
        webbrowser.open_new_tab(
            "http://pylottosimu.readthedocs.io")

    def onClose(self):
        """Close the GUI

        :returns: none"""
        self.ui.close()


class DrawLotto(QtCore.QObject):
    """simulate a lotto draw

    :param name: name of game
    :type name: string
    :param max_draw: maximal draw numbers
    :type max_draw: int
    :param draw_numbers: the draw numbers
    :type draw_numbers: int
    :param with_addit: with additional number
    :type with_addit: bool
    :param addit_numbers: the additional numbers
    :type addit_numbers: int
    :param sep_addit_numbers: separates additional numbers
    :type sep_addit_numbers: bool
    :param max_addit: maximal additional numbers
    :type max_addit: int
    """

    def __init__(self, name='Lotto DE', max_draw=49, draw_numbers=6,
                 with_addit=True, addit_numbers=1, sep_addit_numbers=True,
                 max_addit=9, name_addition="Superzahl"):
        super(DrawLotto, self).__init__()
        self.data = {
            'name': name,
            'max_draw': max_draw,
            'draw_numbers': draw_numbers,
            'with_addit': with_addit,
            'addit_numbers': addit_numbers,
            'sep_addit_numbers': sep_addit_numbers,
            'max_addit': max_addit,
            'name_addition': name_addition
        }

        textselection_tr = [
            self.tr(
                "And now we come to the winning number {0}, it is the {1}."),
            self.tr(
                "The {0} lotto number of today's draw is the {1}."),
            self.tr(
                "We come to the {0} winning number, this is the {1}.",),
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

        self.random_addit = []
        self.random_number = 0
        self.ballbonus = []
        self.ballnumber = []
        self.LastTextnumber = -1

    def draw(self):
        """draw of the lotto numbers

        :returns: none
        """
        if self.data['draw_numbers'] < 1:
            self.data['draw_numbers'] = 1
        drawn_numbers = self.data['draw_numbers']
        if self.data['with_addit']:
            if self.data['sep_addit_numbers']:
                self.random_addit = random.sample(
                    range(1, self.data['max_addit'] + 1),
                    self.data['addit_numbers'])
            else:
                drawn_numbers += self.data['addit_numbers']
        self.random_number = random.sample(range(1, self.data['max_draw'] + 1),
                                           drawn_numbers)
        if self.data['with_addit'] and not self.data['sep_addit_numbers']:
            self.ballnumber = self.random_number[:self.data['draw_numbers']]
            self.ballbonus = self.random_number[self.data['draw_numbers']:
                                                self.data['draw_numbers'] +
                                                self.data['addit_numbers']]
        else:
            self.ballnumber = self.random_number
            self.ballbonus = self.random_addit

    def picknumber(self, turn):
        """pick of a lotto number

        :returns: pick
        """
        try:
            count_number = self.countnumbers[turn]
        except IndexError:
            count_number = turn + 1
        if turn == (self.data['draw_numbers'] - 2) and turn > 0:
            text = self.tr(
                "We are already at the winning number {0}, and thus the "
                "penultimate number of today's draw. It is the {1}.")
            text = str(text).format(count_number,
                                    self.random_number[turn])
        elif turn == (self.data['draw_numbers'] - 1):
            text = self.tr('And now we come to the {0} and last'
                           'winning number, it is the {1}.')
            text = str(text).format(count_number,
                                    self.random_number[turn])

        elif (turn >= (self.data['draw_numbers'] +
                       self.data['addit_numbers']) and
                self.data['with_addit'] is True or
                turn >= (self.data['draw_numbers']) and
                self.data['with_addit'] is False):
            if self.data['with_addit']:
                text_addit_number = "".join(map(" {0:02d}".format, sorted(
                    self.ballbonus[:])))
                textr_addit = self.tr("{1}:{0}, ")
                text_addit = str(textr_addit).format(
                    text_addit_number, self.data['name_addition'])
            else:
                text_addit = ""
            text_random_number = "".join(map(" {0:02d}".format, sorted(
                self.ballnumber[:])))
            text = self.tr("That was today's lottery draw, "
                           "the figures were:{0}, {1}"
                           "I wish you a nice evening! Bye, bye!")
            text = str(text).format(text_random_number, text_addit)
        elif turn == -1:
            if self.data['with_addit']:
                textr_addit = self.tr(
                    "with {number} {name_of_addition_number} ")
                text_addit = str(textr_addit).format(
                    number=self.data['addit_numbers'],
                    name_of_addition_number=self.data['name_addition'])
            else:
                text_addit = ""
            dt = datetime.now()
            textr = self.tr('Welcome to the lottery draw,\n'
                            'at {0}.\nnumbers are drawn: {1} out of {2} {3}!')
            dttext = dt.strftime("%d %B %Y %H:%M")
            if sys.version_info < (3, 0):
                dttext = dttext.decode('utf-8')
            text = str(textr).format(
                dttext, self.data['draw_numbers'],
                self.data['max_draw'], text_addit)
        elif turn == 0:
            textr = self.tr('And the first winning number is the {0}.')
            text = str(textr).format(self.random_number[turn])
            self.LastTextnumber = -1
        elif (turn > (self.data['draw_numbers'] - 1) and
              self.data['with_addit'] is True):
            textr = self.tr('The {name_of_addition_number} is {number}.')
            if self.data['sep_addit_numbers']:
                text = str(textr).format(
                    number=self.random_addit[turn - self.data['draw_numbers']],
                    name_of_addition_number=self.data['name_addition'])
            else:
                text = str(textr).format(
                    number=self.random_number[turn],
                    name_of_addition_number=self.data['name_addition'])
        else:
            text = 'no'
            while True:
                textnumber = randint(0, len(self.textselection) - 1)
                if textnumber != self.LastTextnumber:
                    break
            text = self.textselection[textnumber].format(
                count_number,
                self.random_number[turn])
            self.LastTextnumber = textnumber
        return text
