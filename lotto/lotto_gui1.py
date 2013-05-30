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
from datetime import datetime
import time
from random import randint
from os.path import join
from PyQt4 import QtGui, QtCore

from lotto import Ui_MainWindow as Dlg
from dialog.show_drawing import DlgShowDrawing
from zufallszahl import zufallszahlen


class MeinDialog(QtGui.QMainWindow, Dlg):
    """
    the GUI
    """
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setWindowIcon(QtGui.QIcon(join("misc", "pyLottoSimu.svg")))
        self.setupUi(self)
        self.actionLottosim()
        self.timer = QtCore.QTimer(self)

        # Slots einrichten
        self.connect(self.Zufallsgenerator,
         QtCore.SIGNAL("clicked()"), self.onZufallsgenerator)
        self.connect(self.AusgfeldLeeren,
         QtCore.SIGNAL("clicked()"), self.onAusgfeldLeeren)
        self.connect(self.btn_start,
         QtCore.SIGNAL("clicked()"), self.onbtn_start)
        self.connect(self.actionBeenden,
         QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        self.connect(self.actionInfo,
         QtCore.SIGNAL('triggered()'), self.onInfo)
        self.connect(self.actionLottosimulation, QtCore.SIGNAL("changed()"),
         self.actionLottosim)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.ontimer)
        self.statusBar().showMessage('Bereit')

    def ontimer(self):
        """ start time to show a number"""
        self.timer.stop()
        verz = self.horizontalSlider.value()
        if self.NaechsteZahlverzoegerung >= verz:
            self.NaechsteZahlverzoegerung = verz
        self.NaechsteZahlverzoegerung -= 1
        if self.NaechsteZahlverzoegerung < 10 \
         or (self.NaechsteZahlverzoegerung < 17
         and (self.NaechsteZahlverzoegerung % 2) == 0) \
         or (self.NaechsteZahlverzoegerung < 25
         and (self.NaechsteZahlverzoegerung % 3) == 0) \
         or (self.NaechsteZahlverzoegerung % 4) == 0:
            self.label_zahl.setText(str(zufallszahlen(1,
             int(self.hochste.text()))[0]))
        self.timer.start(100)
        if self.NaechsteZahlverzoegerung < 0:
            self.NaechsteZahl()
            self.NaechsteZahlverzoegerung = verz

    def NaechsteZahl(self):
        """ Display the draw """
        self.label_zahl_2.setText(str(self.zufallszahl[self.durchlauf]))
        self.label_zahl.setText(str(self.zufallszahl[self.durchlauf]))
        if self.durchlauf == (len(self.zufallszahl) - 2):
            text = u'Kommen wir nun zur der {0} Zahl, und damit die vorletzte '\
             u'Zahl der heutigen Ziehung. Es ist die {1}'.\
             format(self.zaehlzahlen[self.durchlauf],
              self.zufallszahl[self.durchlauf])
        elif self.durchlauf == (len(self.zufallszahl) - 1):
            text = u'Und nun kommen wir zu der {0} und letzten Gewinnzahl, '\
             'es ist die {1}'.\
             format(self.zaehlzahlen[self.durchlauf],
              self.zufallszahl[self.durchlauf])
            self.plainTextEdit.appendPlainText(text)
            zufallszahl = sorted(self.zufallszahl[:])
            text1 = "".join(map(" {0:02d}".format, zufallszahl))
            text = u'Das war die heutige Ziehung der Lottozahlen, '\
            u'die Zahlen lauteten:{0}, '\
            u'ich wünsche Ihnen noch einen schönen Abend! '\
            u'Tschüss und auf Wiedersehen!'\
            .format(text1)
            self.timer.stop()
            #show dialog of the draw
            dlg = DlgShowDrawing(self.zufallszahl, self.i_hochste)
            dlg.exec_()
        elif self.durchlauf >= len(self.zufallszahl):
            self.timer.stop()
            text = ''
        elif self.durchlauf == 0:
            text = 'Und die erste Gewinnzahl, ist die {0}'.format(
             self.zufallszahl[self.durchlauf])
            self.LastTextnumber = -1
        else:
            while True:
                Textnumber = randint(0, len(self.textauswahl) - 1)
                if Textnumber != self.LastTextnumber:
                    break
            text = self.textauswahl[Textnumber].format(
             self.zaehlzahlen[self.durchlauf],
             self.zufallszahl[self.durchlauf])
            self.LastTextnumber = Textnumber
        self.plainTextEdit.appendPlainText(text)
        self.durchlauf += 1

    def onbtn_start(self):
        """ start simultion with the first drawing
        init timer with the valve from the Scrollbar
        the next drawing starts with the timer event
        """
        self.plainTextEdit.setPlainText("")
        self.label_zahl_2.setText("")
        self.durchlauf = 0
        dt = datetime.now()
        i_anzahl = int(self.anzahl.text())
        self.i_hochste = int(self.hochste.text())
        self.zufallszahl = zufallszahlen(i_anzahl, self.i_hochste)
        text = 'Willkommen bei der Ziehung der Lottozahlen, \n am {0}, \n'\
         'Ausgelost werden: {1} aus {2}!'.format(
         dt.strftime("%d %B %Y um %H:%M"), i_anzahl, self.i_hochste)
        self.plainTextEdit.appendPlainText(text)
        self.timer.start(100)
        self.NaechsteZahlverzoegerung = self.horizontalSlider.value()
        self.textauswahl = [
            u'Und nun kommen wir zu der {0}. Gewinnzahl, es ist die {1}',
            u'Die {0} Lottozahl der heutigen Ziehung ist die {1}',
            u'Kommen wir nun zur {0} Gewinnzahl, dies ist die {1}',
            u'Kommen wir nun zur {0} Zahl der heutigen Ziehung {1}',
            u'Die {0} Gewinnzahl lautet {1}']
        self.zaehlzahlen = ['ersten', 'zweiten', 'dritten', 'vierten',
        u'fünften', 'sechsten', 'siebten', 'achten', 'neunten']
        i = 10
        while i < len(self.zufallszahl):
            self.zaehlzahlen.append(str(i) + ".")
            i += 1

    def actionLottosim(self):
        """ Changing the layout for simulation or generation
        Move the textedit and change the visible
        """
        self.plainTextEdit.setPlainText("")
        if self.actionLottosimulation.isChecked():
            # Lottosimulation
            self.statusBar().showMessage('Lottosimulation')
            self.plainTextEdit.setGeometry(QtCore.QRect(20, 180, 441, 136))
            self.Zufallsgenerator.setVisible(False)
            self.AusgfeldLeeren.setVisible(False)
            self.label_Lottozahlen.setVisible(False)
            self.label_zahl.setVisible(True)
            self.label_zahl_2.setVisible(True)
            self.label_Geschwindigkeit.setVisible(True)
            self.label_zahl.setText("")
            self.label_zahl_2.setText("")
            self.btn_start.setVisible(True)
            self.horizontalSlider.setVisible(True)

        else:
            # Zufallsgenerator
            self.statusBar().showMessage('Zufallsgenerator')
            self.plainTextEdit.setGeometry(QtCore.QRect(20, 20, 441, 111))
            self.Zufallsgenerator.setVisible(True)
            self.AusgfeldLeeren.setVisible(True)
            self.label_Lottozahlen.setVisible(True)
            self.label_zahl.setVisible(False)
            self.label_zahl_2.setVisible(False)
            self.label_Geschwindigkeit.setVisible(False)
            self.btn_start.setVisible(False)
            self.horizontalSlider.setVisible(False)

    def onZufallsgenerator(self):
        """ Show the output from the random number generator """
        i_anzahl = int(self.anzahl.text())
        i_hochste = int(self.hochste.text())
        zufallszahl = sorted(zufallszahlen(i_anzahl, i_hochste))
        if zufallszahl:
            text = "".join(map(" {0:02d}".format, zufallszahl))
        else:
            text = "Fehler, keine gültigen Zahlen vorhanden!"
        dt = datetime.now()
        text = dt.strftime("%H:%M:%S: ") + str(i_anzahl) + \
         " aus " + str(i_hochste) + ": " + text
        self.plainTextEdit.appendPlainText(text)

    def onAusgfeldLeeren(self):
        """ clear the TextEdit"""
        self.plainTextEdit.setPlainText("")

    def onInfo(self):
        """ Infoscreen """
        text = 'Zufallsgenerator und Simulation einer Ziehung\n\n' \
        'Die Idee der Simulation ist von imageupload,\n' \
        'dem Betreiber von http://www.my-image-upload.de/\n\n' \
        'Lizenz: GNU GPL v3\n' \
        'http://www.gnu.org/licenses/'
        a = QtGui.QMessageBox()
        a.setWindowTitle('Info')
        a.setText(text)
        a.setInformativeText('Erstellt mit Python von Markus Hackspacher')
        a.exec_()


def gui():
    """open the GUI"""
    app = QtGui.QApplication(sys.argv)
    dialog = MeinDialog()
    dialog.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    gui()
