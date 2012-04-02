#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Das Hauptprogramm

Das Programm hat die Creative Commons by-sa Lizenz
http://creativecommons.org/licenses/by-sa/3.0/deed.de
"""

import sys 
from datetime import datetime
import time
from random import randint
from PyQt4 import QtGui, QtCore 

from lotto import Ui_MainWindow as Dlg
from zufallszahl import zufallszahlen

class MeinDialog(QtGui.QMainWindow, Dlg): 
   def __init__(self): 
       QtGui.QDialog.__init__(self) 
       self.setupUi(self)
       self.actionLottosim()
       self.timer =  QtCore.QTimer( self )

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
       self.connect(self.actionLottosimulation, QtCore.SIGNAL("changed()"), self.actionLottosim)
       self.connect( self.timer, QtCore.SIGNAL("timeout()"), self.ontimer )
       self.statusBar().showMessage('Bereit')

   def ontimer(self):
       """ Ausgabe der nächsten Zahl """
       verz = self.horizontalSlider.value() * 50
       self.timer.start(verz)
       self.label_zahl.setText(str(self.zufallszahl[self.durchlauf]))
       if self.durchlauf == (len(self.zufallszahl)-3):
           text = u'Kommen wir nun zur der {0} Zahl, und damit die vorletze Zahl der heutigen Ziehung.. Es ist die {1}'.\
            format( self.zaehlzahlen[ self.durchlauf], self.zufallszahl[ self.durchlauf])
       elif self.durchlauf == (len(self.zufallszahl)-2):
           text = u'Und nun kommen wir zu der {0} und letzten Gewinnzahl, es ist die {1}'.\
            format( self.zaehlzahlen[self.durchlauf], self.zufallszahl[ self.durchlauf])
       elif self.durchlauf == len(self.zufallszahl)-1:
           text = 'So, und dies ist die Zusatzzahl .. Es ist die {0}'\
            .format(self.zufallszahl[self.durchlauf])
           self.plainTextEdit.appendPlainText(text)
           text1=''
           zufallszahl=sorted(self.zufallszahl[:-1])
           text1 = "".join(map(" {0:02d}".format, zufallszahl))
           text = u'Das war die heutige Ziehung der Lottozahlen, '\
            + u'die Zahlen lauteten:{0}, die Zusatzzahl: {1}, '.format(text1,self.zufallszahl[-1])\
            + u'ich wünsche Ihnen noch einen schönen Abend! Tschüss und auf Wiedersehen!'
           self.timer.stop()
       elif self.durchlauf >= len(self.zufallszahl):
           self.timer.stop()
           text = ''           
       elif self.durchlauf == 0:
           text = 'Und die erste Gewinnzahl, ist die {0}'.format( self.zufallszahl[self.durchlauf])      
       else:
           text = self.textauswahl[ randint(0 ,len(self.textauswahl))]\
            .format( self.zaehlzahlen[self.durchlauf], self.zufallszahl[self.durchlauf])
       self.plainTextEdit.appendPlainText( text)
       self.durchlauf += 1
        
   def onbtn_start(self):
       """ start simultion with the first drawing
       
       init timer with the valve from the Scrollbar
       
       the next drawing starts with the timer event
       """
       self.plainTextEdit.setPlainText("")
       self.durchlauf  = 0
       dt = datetime.now()
       i_anzahl = int(self.anzahl.text())
       i_hochste = int(self.hochste.text())
       self.zufallszahl = zufallszahlen(i_anzahl+1,i_hochste)
       text = 'Willkommen bei der Ziehung der Lottozahlen, \n am {0}, \nAusgelost werden: {1} aus {2}!'
       text = text.format(dt.strftime("%d %B %Y um %H:%M"), i_anzahl, i_hochste)
       self.plainTextEdit.appendPlainText(text)
       verz = self.horizontalSlider.value()  * 20
       self.timer.start(verz)
       self.textauswahl = [ u'Und nun kommen wir zu der {0}. Gewinnzahl, es ist die {1}',\
            u'Die {0} Lottozahl der heutigen Ziehung ist die {1}',\
            u'Kommen wir nun zur {0} Gewinnzahl, dies ist die {1}',\
            u'Kommen wir nun zur {0} Zahl der heutigen Ziehung {1}',\
            u'Die {0} Gewinnzahl lautet {1}']
       self.zaehlzahlen = [ 'ersten', 'zweiten', 'dritten', 'vierten', u'fünften', 'sechsten', 'siebten',\
        'achten', 'neunten']
       i=10
       while i < len( self.zufallszahl):
           self.zaehlzahlen.append( str(i) + ".")
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
           self.label_Geschwindigkeit.setVisible(True)
           self.label_zahl.setText("")
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
       text = dt.strftime("%H:%M:%S: ") + str(i_anzahl) + " aus " + str(i_hochste) + ": " + text
       self.plainTextEdit.appendPlainText(text)
  
   def onAusgfeldLeeren(self):
       # clear the TextEdit
       self.plainTextEdit.setPlainText("")

   def onInfo(self):
        # Infoscreen
        text = 'Zufallsgenerator und Simulation einer Ziehung\n\n'
        text += 'Die Idee der Simulation ist\n'
        text = text + 'von imageupload dem Betreiber von \nhttp://www.my-image-upload.de/\n\n'
        text = text + 'Lizenz: Creative Commons by-sa\n'
        text = text + 'http://creativecommons.org/licenses/by-sa/3.0/deed.de'
        a = QtGui.QMessageBox()
        a.setWindowTitle('Info')
        a.setText(text)
        a.setInformativeText('Erstellt mit Python von Markus Hackspacher')
        a.exec_()
        
def gui():
    app = QtGui.QApplication(sys.argv) 
    dialog = MeinDialog() 
    dialog.show() 
    sys.exit(app.exec_())

if __name__ == "__main__":
    gui()
