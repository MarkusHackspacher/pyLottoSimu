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
    if QtCore.QT_VERSION >= 0x050000:
        import pylottosimu.lottokugeln_rc3_qt5 as lottokugeln_rc
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

        self.turn = 0
        self.random_number = 0
        self.delay_of_next_number = self.ui.horizontalSlider.value()
        self.lottodraw = drawlotto()
        self.ui.label_numbers.setText(self.lottodraw.data['name'])
        self.ui.show()

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
                    self.lottodraw.data['max_draw']) + 1), 1)[0]))
        self.timer.start(100)
        if self.delay_of_next_number < 0:
            self.show_next_number()
            self.delay_of_next_number = verz

    def show_next_number(self):
        """Simulation of the draw and show the next Number on the Screen.
        @return: none
        """
        if self.turn == 0:
            self.ui.btn_draw_overview.setVisible(False)
            self.LastTextnumber = -1

        if self.turn >= len((self.lottodraw.random_number
                             + self.lottodraw.random_addit)):
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
        @return: none
        """
        dlgdraw = DlgShowDrawing(self.lottodraw.random_number,
                                 self.lottodraw.data['max_draw'])
        dlgdraw.exec_()

    def onsystem(self):
        """show dialog of the draw
        @return: none
        """
        sysdat = DlgLottoSystem.lottosystemdata()
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
        @return: none
        """
        self.ui.label_last_draw_number.setText("")
        self.turn = 0
        self.lottodraw.draw()
        self.ui.plaintextedit.setPlainText(self.lottodraw.picknumber(-1))
        self.timer.start(100)
        self.delay_of_next_number = self.ui.horizontalSlider.value()

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
        self.lottodraw.draw()
        if self.lottodraw.random_number:
            text = "".join(map(" {0:02d}".format, sorted(
                self.lottodraw.random_number)))
        else:
            text = self.tr("Error, no valid numbers available!")
        dt = datetime.now()
        texttr = self.tr("{} {} out of {}: {}")
        text = unicode(texttr).format(dt.strftime("%H:%M:%S:"),
                                      self.lottodraw.data['draw_numbers'],
                                      self.lottodraw.data['max_draw'],
                                      text)
        self.ui.plaintextedit.appendPlainText(text)

    def onclean_output_text(self):
        """Clean the output text
        @return: none"""
        self.ui.plaintextedit.setPlainText("")

    def oninfo(self):
        """info message box
        @return: none"""
        infobox = QtWidgets.QMessageBox()
        infobox.setWindowTitle(self.tr('Info'))
        text = self.tr(
            'simulation of a random draw\n\n'
            'based on an idea of imageupload,\n'
            'http://www.my-image-upload.de/\n\n'
            'GNU GPL v3\n'
            'http://www.gnu.org/licenses/')
        infobox.setText(text)
        text = self.tr('Created with Python by Markus Hackspacher '
                       'http://markush.cwsurf.de')
        infobox.setInformativeText(text)
        infobox.exec_()

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


class drawlotto(QtCore.QObject):
    def __init__(self, name='Lotto DE', max_draw=49, draw_numbers=6,
                 with_addit=False, addit_numbers=0, sep_addit_numbers=False,
                 max_addit=0):
        """simulate a lotto draw
        @param name: name of game
        @type name: string
        @param max_draw: maximal draw numbers
        @type max_draw: int
        @param draw_numbers: the draw numbers
        @type draw_numbers: int
        @param with_addit: with additional number
        @type with_addit: bool
        @param addit_numbers: the additional numbers
        @type addit_numbers: int
        @param sep_addit_numbers: separates additional numbers
        @type sep_addit_numbers: bool
        @param max_addit: maximal additional numbers
        @type max_addit: int
        """
        QtWidgets.QDialog.__init__(self)
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

    def draw(self):
        """draw of the lotto numbers
        @return: none
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

    def picknumber(self, turn):
        """pick of a lotto number
        @return: pick
        """
        if turn == (self.data['draw_numbers'] - 2):
            text = self.tr(
                "We are already at the winning number {0}, and thus the "
                "penultimate number of today's draw. It is the {1}.")
            text = unicode(text).format(self.countnumbers[turn],
                                        self.random_number[turn])
        elif turn == (self.data['draw_numbers'] - 1):
            text = self.tr('And now we come to the {0} and last'
                           'winning number, it is the {1}.')
            text = unicode(text).format(self.countnumbers[turn],
                                        self.random_number[turn])

        elif (turn >= (self.data['draw_numbers'] + self.data['addit_numbers'])
                and self.data['with_addit'] is True
                or turn >= (self.data['draw_numbers'])
                and self.data['with_addit'] is False):
            if self.data['with_addit']:
                text_addit_number = "".join(map(" {0:02d}".format, sorted(
                    self.random_addit[:])))
                textr_addit = self.tr("the additional numbers are{0}, ")
                text_addit = unicode(textr_addit).format(text_addit_number)
            else:
                text_addit = ""
            text_random_number = "".join(map(" {0:02d}".format, sorted(
                self.random_number[:])))
            text = self.tr("That was today's lottery draw, "
                           "the figures were:{0}, {1}"
                           "I wish you a nice evening! Bye, bye!")
            text = unicode(text).format(text_random_number, text_addit)
        elif turn == -1:
            if self.data['with_addit']:
                textr_addit = self.tr("with {0} additional numbers ")
                text_addit = unicode(textr_addit).format(
                    self.data['addit_numbers'])
            else:
                text_addit = ""
            dt = datetime.now()
            textr = self.tr('Welcome to the lottery draw,\n'
                            'at {0}.\nnumbers are drawn: {1} out of {2} {3}!')
            dttext = dt.strftime("%d %B %Y um %H:%M")
            if sys.version_info < (3, 0):
                dttext = dttext.decode('utf-8')
            text = unicode(textr).format(
                dttext,
                self.data['draw_numbers'],
                self.data['max_draw'],
                text_addit)
        elif turn == 0:
            textr = self.tr('And the first winning number is the {0}.')
            text = unicode(textr).format(self.random_number[turn])
            self.LastTextnumber = -1
        elif turn > (self.data['draw_numbers'] - 1):
            if self.data['with_addit'] is True:
                textr = self.tr('The additional number is the {0}.')
                if self.data['sep_addit_numbers']:
                    text = unicode(textr).format(self.random_addit[turn
                                                 - self.data['draw_numbers']])
                else:
                    text = unicode(textr).format(self.random_number[turn])
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


def gui(arguments):
    """Open the GUI
    @param arguments: language, see in folder translate
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
    # gui('')
    locale = str(QtCore.QLocale.system().name())
    app = QtWidgets.QApplication(sys.argv)
    translator = QtCore.QTranslator()
    translator.load(os.path.abspath(os.path.join(os.path.dirname(__file__),
                    "translation", "lotto1_" + locale)))
    app.installTranslator(translator)
    lt = drawlotto(with_addit=False, addit_numbers=2, sep_addit_numbers=True,
                   max_addit=10)
    lt.draw()
    print(lt.random_number, lt.random_addit)
    print(lt.random_number + lt.random_addit)
    print(lt.picknumber(-1))
    for x in range(len(lt.random_number + lt.random_addit) + 1):
        print(lt.picknumber(x))
    lt.data['with_addit'] = True
    lt.draw()
    print(lt.random_number, lt.random_addit)
    print(lt.random_number + lt.random_addit)
    print(lt.picknumber(-1))
    for x in range(len(lt.random_number + lt.random_addit) + 1):
        print(lt.picknumber(x))
