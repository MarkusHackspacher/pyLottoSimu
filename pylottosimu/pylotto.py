#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyLottoSimu

# Copyright (C) <2012-2015> Markus Hackspacher

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

from __future__ import absolute_import

import os
import sys
import webbrowser
from datetime import datetime
from random import randint
import random

import pylottosimu.dialog.lottosettingdialog as DlgLottoSystem
from pylottosimu.dialog.show_drawing import DlgShowDrawing
from pylottosimu.lottosystem import lottosystemdata

_FORCE_PYSIDE = False

try:
    if _FORCE_PYSIDE:
        raise ImportError('_FORCE_PYSIDE')
    from PyQt5 import QtGui, QtCore, QtWidgets, uic
    from PyQt5.QtSvg import QSvgWidget

    def QtLoadUI(uifile):
        return uic.loadUi(uifile)

except ImportError:
    try:
        from PySide import QtGui, QtCore
        from PySide import QtGui as QtWidgets
        from PySide.QtSvg import QSvgWidget

        def QtLoadUI(uifile):
            from PySide import QtUiTools
            loader = QtUiTools.QUiLoader()
            uif = QtCore.QFile(uifile)
            uif.open(QtCore.QFile.ReadOnly)
            result = loader.load(uif)
            uif.close()
            return result
    except ImportError:
        from PyQt4 import QtGui, QtCore
        from PyQt4 import QtGui as QtWidgets
        from PyQt4.QtSvg import QSvgWidget
        def QtLoadUI(uifile):
            return uic.loadUi(uifile)

if sys.version_info < (3, 0):
    range = xrange
    str = unicode

__doc__ = "The signals for the GUI"


class LottoSimuDialog(QtWidgets.QMainWindow):
    """The GUI and program of the pyLottoSimu.
    """
    def __init__(self):
        """Initial user interface and slots

        :returns: none
        """
        super(LottoSimuDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = QtLoadUI(os.path.abspath(os.path.join(
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

        self.turn = 0
        self.random_number = 0
        self.delay_of_next_number = self.ui.horizontalSlider.value()
        self.lottodraw = drawlotto()
        self.ui.label_numbers.setText(self.lottodraw.data['name'])
        self.ui.show()

    def ontimer(self):
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
            self.show_next_number()
            self.delay_of_next_number = verz

    def show_next_number(self):
        """Simulation of the draw and show the next Number on the Screen.

        :returns: none
        """
        if self.turn == 0:
            self.ui.btn_draw_overview.setVisible(False)
            self.LastTextnumber = -1

        if self.turn >= len((self.lottodraw.random_number +
                             self.lottodraw.random_addit)):
            self.timer.stop()
            text = ''
            if self.ui.rdbtn_show_draw_after.isChecked():
                self.onbtn_draw_overview()
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

    def onbtn_draw_overview(self):
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

    def onsystem(self):
        """show dialog of the draw

        :returns: none
        """
        sysdat = lottosystemdata()
        system = DlgLottoSystem.LottoSettingsDialog.getValues(sysdat)

        if system[1]:
            self.lottodraw.data['name'] = system[0][0]
            self.lottodraw.data['max_draw'] = system[0][1]
            self.lottodraw.data['draw_numbers'] = system[0][2]
            self.lottodraw.data['with_addit'] = system[0][3]
            self.lottodraw.data['addit_numbers'] = system[0][4]
            self.lottodraw.data['sep_addit_numbers'] = system[0][5]
            self.lottodraw.data['max_addit'] = system[0][6]

        self.ui.label_numbers.setText(self.lottodraw.data['name'])
        self.ui.btn_draw_overview.setVisible(False)

    def onbtn_start(self):
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

    def action_lottosim(self):
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

    def onrandom_numbers_generator(self):
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
        texttr = self.tr("{} {} out of {}: {}")
        text = str(texttr).format(dt.strftime("%H:%M:%S:"),
                                  self.lottodraw.data['draw_numbers'],
                                  self.lottodraw.data['max_draw'], text)
        self.ui.plaintextedit.appendPlainText(text)

    def onclean_output_text(self):
        """Clean the output text

        :returns: none"""
        self.ui.plaintextedit.setPlainText("")

    def oninfo(self):
        """info message box

        :returns: none"""
        infobox = QtWidgets.QMessageBox()
        infobox.setWindowTitle(self.tr('Info'))
        text = self.tr(
            'simulation of a random draw\n\n'
            'based on an idea of imageupload,\n'
            'http://www.my-image-upload.de/\n\n'
            'GNU GPL v3\n'
            'http://www.gnu.org/licenses/')
        infobox.setText(text)
        text = self.tr('More Information about the program at '
                       'http://pylottosimu.readthedocs.org')
        infobox.setInformativeText(text)
        infobox.exec_()

    def onwebsite(self):
        """Open website

        :returns: none
        """
        webbrowser.open_new_tab(
            "http://pylottosimu.readthedocs.org")

    def onclose(self):
        """Close the GUI

        :returns: none"""
        self.ui.close()


class drawlotto(QtCore.QObject):
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
                 with_addit=False, addit_numbers=0, sep_addit_numbers=False,
                 max_addit=0):
        super(drawlotto, self).__init__()
        self.data = {
            'name': name,
            'max_draw': max_draw,
            'draw_numbers': draw_numbers,
            'with_addit': with_addit,
            'addit_numbers': addit_numbers,
            'sep_addit_numbers': sep_addit_numbers,
            'max_addit': max_addit}

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

    def draw(self):
        """draw of the lotto numbers

        :returns: none
        """
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
        if turn == (self.data['draw_numbers'] - 2):
            text = self.tr(
                "We are already at the winning number {0}, and thus the "
                "penultimate number of today's draw. It is the {1}.")
            text = str(text.format(self.countnumbers[turn],
                                   self.random_number[turn]))
        elif turn == (self.data['draw_numbers'] - 1):
            text = self.tr('And now we come to the {0} and last'
                           'winning number, it is the {1}.')
            text = str(text).format(self.countnumbers[turn],
                                    self.random_number[turn])

        elif (turn >= (self.data['draw_numbers'] +
                       self.data['addit_numbers']) and
                self.data['with_addit'] is True or
                turn >= (self.data['draw_numbers']) and
                self.data['with_addit'] is False):
            if self.data['with_addit']:
                text_addit_number = "".join(map(" {0:02d}".format, sorted(
                    self.ballbonus[:])))
                if len(self.ballbonus) > 1:
                    textr_addit = self.tr("the bonus numbers are{0}, ")
                else:
                    textr_addit = self.tr("the bonus number is{0}, ")
                text_addit = str(textr_addit).format(text_addit_number)
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
                textr_addit = self.tr("with {0} additional numbers ")
                text_addit = str(textr_addit).format(
                    self.data['addit_numbers'])
            else:
                text_addit = ""
            dt = datetime.now()
            textr = self.tr('Welcome to the lottery draw,\n'
                            'at {0}.\nnumbers are drawn: {1} out of {2} {3}!')
            dttext = dt.strftime("%d %B %Y um %H:%M")
            if sys.version_info < (3, 0):
                dttext = dttext.decode('utf-8')
            text = str(textr).format(
                dttext,
                self.data['draw_numbers'],
                self.data['max_draw'],
                text_addit)
        elif turn == 0:
            textr = self.tr('And the first winning number is the {0}.')
            text = str(textr).format(self.random_number[turn])
            self.LastTextnumber = -1
        elif turn > (self.data['draw_numbers'] - 1):
            if self.data['with_addit'] is True:
                textr = self.tr('The additional number is the {0}.')
                if self.data['sep_addit_numbers']:
                    text = str(textr).format(self.random_addit[turn -
                                             self.data['draw_numbers']])
                else:
                    text = str(textr).format(self.random_number[turn])
        else:
            text = 'no'
            while True:
                textnumber = randint(0, len(self.textselection) - 1)
                if textnumber != self.LastTextnumber:
                    break
            text = self.textselection[textnumber].format(
                self.countnumbers[turn],
                self.random_number[turn])
            self.LastTextnumber = textnumber
        return text
