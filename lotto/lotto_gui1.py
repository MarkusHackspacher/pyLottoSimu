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
from PyQt4 import QtGui, QtCore, uic

import lottokugeln_rc
from dialog.show_drawing import DlgShowDrawing
from zufallszahl import zufallszahlen


class MeinDialog(QtGui.QMainWindow):
    """
    the GUI
    """
    def __init__(self):
        QtGui.QDialog.__init__(self)
        
        # Set up the user interface from Designer.
        self.ui = uic.loadUi(join("lotto", "lotto.ui"))
        self.ui.setWindowIcon(QtGui.QIcon(join("misc", "pyLottoSimu.svg")))
 
        self.actionLottosim()
        self.timer = QtCore.QTimer(self)

        self.ui.show()
        # Slots einrichten
        self.connect(self.ui.Zufallsgenerator,
         QtCore.SIGNAL("clicked()"), self.onZufallsgenerator)
        self.connect(self.ui.AusgfeldLeeren,
         QtCore.SIGNAL("clicked()"), self.onAusgfeldLeeren)
        self.connect(self.ui.btn_start,
         QtCore.SIGNAL("clicked()"), self.onbtn_start)
        self.connect(self.ui.actionBeenden,
         QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        self.connect(self.ui.actionInfo,
         QtCore.SIGNAL('triggered()'), self.onInfo)
        self.connect(self.ui.actionLottosimulation, QtCore.SIGNAL("changed()"),
         self.actionLottosim)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.ontimer)
        self.ui.statusBar().showMessage('Bereit')
        verz = self.ui.horizontalSlider.value()
        self.NaechsteZahlverzoegerung = verz

    def ontimer(self):
        """ start time to show a number"""
        self.timer.stop()
        verz = self.ui.horizontalSlider.value()
        if self.NaechsteZahlverzoegerung >= verz:
            self.NaechsteZahlverzoegerung = verz
        self.NaechsteZahlverzoegerung -= 1
        if self.NaechsteZahlverzoegerung < 10 \
         or (self.NaechsteZahlverzoegerung < 17
         and (self.NaechsteZahlverzoegerung % 2) == 0) \
         or (self.NaechsteZahlverzoegerung < 25
         and (self.NaechsteZahlverzoegerung % 3) == 0) \
         or (self.NaechsteZahlverzoegerung % 4) == 0:
            self.ui.label_zahl.setText(str(zufallszahlen(1,
             int(self.ui.hochste.text()))[0]))
        self.timer.start(100)
        if self.NaechsteZahlverzoegerung < 0:
            self.NaechsteZahl()
            self.NaechsteZahlverzoegerung = verz

    def NaechsteZahl(self):
        """ Display the draw """
        self.ui.label_zahl_2.setText(str(self.zufallszahl[self.durchlauf]))
        self.ui.label_zahl.setText(str(self.zufallszahl[self.durchlauf]))
        if self.durchlauf == (len(self.zufallszahl) - 2):
            text = self.tr(u'Kommen wir nun zur der {0} Zahl, und damit die vorletzte '\
             u'Zahl der heutigen Ziehung. Es ist die {1}'.\
             format(self.zaehlzahlen[self.durchlauf],
              self.zufallszahl[self.durchlauf]))
        elif self.durchlauf == (len(self.zufallszahl) - 1):
            text = self.tr(u'Und nun kommen wir zu der {0} und letzten Gewinnzahl, '\
             'es ist die {1}'.\
             format(self.zaehlzahlen[self.durchlauf],
              self.zufallszahl[self.durchlauf]))
            self.ui.plainTextEdit.appendPlainText(text)
            zufallszahl = sorted(self.zufallszahl[:])
            text1 = "".join(map(" {0:02d}".format, zufallszahl))
            text = self.tr(u'Das war die heutige Ziehung der Lottozahlen, '\
            u'die Zahlen lauteten:{0}, '\
            u'ich wünsche Ihnen noch einen schönen Abend! '\
            u'Tschüss und auf Wiedersehen!'\
            .format(text1))
            self.timer.stop()
            #show dialog of the draw
            dlgdraw = DlgShowDrawing(self.zufallszahl, self.i_hochste)
            dlgdraw.exec_()
        elif self.durchlauf >= len(self.zufallszahl):
            self.timer.stop()
            text = ''
        elif self.durchlauf == 0:
            text = self.tr('Und die erste Gewinnzahl, ist die {0}'.format(
             self.zufallszahl[self.durchlauf]))
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
        self.ui.plainTextEdit.appendPlainText(text)
        self.durchlauf += 1

    def onbtn_start(self):
        """ start simultion with the first drawing
        init timer with the valve from the Scrollbar
        the next drawing starts with the timer event
        """
        self.ui.plainTextEdit.setPlainText("")
        self.ui.label_zahl_2.setText("")
        self.durchlauf = 0
        dt = datetime.now()
        i_anzahl = int(self.ui.anzahl.text())
        self.i_hochste = int(self.ui.hochste.text())
        self.zufallszahl = zufallszahlen(i_anzahl, self.i_hochste)
        text = self.tr('Willkommen bei der Ziehung der Lottozahlen, \n am {0}, \n'\
         'Ausgelost werden: {1} aus {2}!'.format(
         dt.strftime("%d %B %Y um %H:%M"), i_anzahl, self.i_hochste))
        self.ui.plainTextEdit.appendPlainText(text)
        self.timer.start(100)
        self.NaechsteZahlverzoegerung = self.ui.horizontalSlider.value()
        self.textauswahl = [
            u'Und nun kommen wir zu der {0} Gewinnzahl, es ist die {1}',
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
        self.ui.plainTextEdit.setPlainText("")
        if self.ui.actionLottosimulation.isChecked():
            # Lottosimulation
            self.ui.statusBar().showMessage('Lottosimulation')
            self.ui.plainTextEdit.setGeometry(QtCore.QRect(20, 180, 441, 136))
            self.ui.Zufallsgenerator.setVisible(False)
            self.ui.AusgfeldLeeren.setVisible(False)
            self.ui.label_Lottozahlen.setVisible(False)
            self.ui.label_zahl.setVisible(True)
            self.ui.label_zahl_2.setVisible(True)
            self.ui.label_Geschwindigkeit.setVisible(True)
            self.ui.label_zahl.setText("")
            self.ui.label_zahl_2.setText("")
            self.ui.btn_start.setVisible(True)
            self.ui.horizontalSlider.setVisible(True)

        else:
            # Zufallsgenerator
            self.ui.statusBar().showMessage('Zufallsgenerator')
            self.ui.plainTextEdit.setGeometry(QtCore.QRect(20, 20, 441, 111))
            self.ui.Zufallsgenerator.setVisible(True)
            self.ui.AusgfeldLeeren.setVisible(True)
            self.ui.label_Lottozahlen.setVisible(True)
            self.ui.label_zahl.setVisible(False)
            self.ui.label_zahl_2.setVisible(False)
            self.ui.label_Geschwindigkeit.setVisible(False)
            self.ui.btn_start.setVisible(False)
            self.ui.horizontalSlider.setVisible(False)

    def onZufallsgenerator(self):
        """ Show the output from the random number generator """
        i_anzahl = int(self.ui.anzahl.text())
        i_hochste = int(self.ui.hochste.text())
        zufallszahl = sorted(zufallszahlen(i_anzahl, i_hochste))
        if zufallszahl:
            text = "".join(map(" {0:02d}".format, zufallszahl))
        else:
            text = self.tr("Fehler, keine gültigen Zahlen vorhanden!")
        dt = datetime.now()
        text = dt.strftime("%H:%M:%S: ") + str(i_anzahl) + \
         " aus " + str(i_hochste) + ": " + text
        self.ui.plainTextEdit.appendPlainText(text)

    def onAusgfeldLeeren(self):
        """ clear the TextEdit"""
        self.ui.plainTextEdit.setPlainText("")

    def onInfo(self):
        """ Infoscreen """
        text = self.tr(
        'Zufallsgenerator und Simulation einer Ziehung\n\n' \
        'Die Idee der Simulation ist von imageupload,\n' \
        'dem Betreiber von http://www.my-image-upload.de/\n\n' \
        'Lizenz: GNU GPL v3\n' \
        'http://www.gnu.org/licenses/')
        a = QtGui.QMessageBox()
        a.setObjectName('Info')
        a.setWindowTitle('Info')
        a.setText(text)
        text = self.tr('Erstellt mit Python von Markus Hackspacher')
        a.setInformativeText(text)
        a.exec_()


def gui():
    """open the GUI"""
    app = QtGui.QApplication(sys.argv)
    locale=unicode(QtCore.QLocale.system().name())
    print "lotto1_" + unicode(locale)
    translator = QtCore.QTranslator()
    translator.load(join("lotto","lotto1_" + unicode(locale)))
    app.installTranslator(translator)
    dialog = MeinDialog()
    sys.exit(app.exec_())

if __name__ == "__main__":
    gui()
