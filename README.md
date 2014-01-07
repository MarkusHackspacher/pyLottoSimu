
===========
pyLottoSimu
===========

Lotto Generator und Simulator

a programm for the german lottery "pick 6 out of 49" system.

install
-------

The program requires [Python 2.7](www.python.org/download/) and [Qt4 for Python 2.7](www.riverbankcomputing.com/software/pyqt/download).

Start with
```python lotto.pyw [de|fr|es|it|ru]```

Make the documentation as .pdf file:
```epydoc pylottosimu.pyw lotto --pdf```

To translate the programm or make a translation in your language,
insert in the complete.pro your language code.
```
cd lotto
pylupdate4 complete.pro
```
translate your language file: lotto1_xx.ts, and produce the .ts translation files with
```
lrelease complete.pro
```

Installieren
-------------

Das Programm läuft auf MacOS, Windows und Linux,
und überall dort wo Python und pyqt installieren lässt!

Das Programm benötigt [Python 2.7](www.python.org/download/) und [Qt4 für Python 2.7](www.riverbankcomputing.com/software/pyqt/download) dazu.

Start mit: 
```python lotto.pyw [de|fr|es|it|ru]```

Documentation als .pdf Datei aus den Kommentaren des Quelltextes erstellen lassen:
```epydoc pylottosimu.pyw lotto --pdf```

Bedienen
---------
Der Modus kann in der Menüleiste angewählt werden
Anzahl der Zufallszahlen sind zwischen 1 bis 15 wählbar sowie der
 Zahlenbereich zwischen 20 und 90! 

Modus Zufallsgenerator:
Die Zahlen auswählen und mit 'Zufallsgenerator ein' starten

Modus Simulation:
Die Zahlen auswählen und mit 'Start' die Simulation starten.
Dabei kann mit dem Schieber oben links die Geschwindigkeit verändert werden.

Auf der Webseite gibt es [Videos](http://markush.cwsurf.de/joomla_17/index.php/python/pylottosimu/8-lotto-generator-und-simulator) zu dem Programm.

Info und Lizenz
---------------

pyLottoSimu

Copyright <2012-2014> Markus Hackspacher

This file is part of pyLottoSimu.

pyLottoverwaltung is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyLottoSimu is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyLottoSimu.  If not, see <http://www.gnu.org/licenses/>.

