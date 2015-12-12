pyLottoSimu
===========

![Github Releases](https://img.shields.io/github/release/markushackspacher/pylottosimu.svg)
![Stars](https://img.shields.io/github/stars/MarkusHackspacher/pyLottoSimu.svg)
[![license-GPLv3](https://img.shields.io/badge/license-GPLv3-blue.svg)]
(https://github.com/MarkusHackspacher/pyLottoSimu/blob/master/LICENSE)
[![Join the chat at https://gitter.im/MarkusHackspacher/pyLottoSimu](https://badges.gitter.im/Join%20Chat.svg)]
(https://gitter.im/MarkusHackspacher/pyLottoSimu?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Documentation Status](https://readthedocs.org/projects/pylottosimu/badge/?version=latest)]
(https://readthedocs.org/projects/pylottosimu/?badge=latest)
[![Build Status](https://drone.io/github.com/MarkusHackspacher/pyLottoSimu/status.png)]
(https://drone.io/github.com/MarkusHackspacher/pyLottoSimu/latest)

Lotto Generator und Simulator

a simulation of Lotto Germany (pick 6 out of 49), Lotto Austria (pick 6 out of 45), EuroMillionen, Powerball Lottery US and Mega Millions lottery system.

install
-------

The program requires [Python 2.7 or 3.x](http://www.python.org/download/) 
and [Qt5 for Python](http://www.riverbankcomputing.com/software/pyqt/download5).

Start with

`python lotto.pyw [de|fr|es|it|ru]`

Make the documentation as .html file:

```
cd docs
make html
```

To translate the program or make a translation in your language,
insert in the complete.pro your language code.

```
cd pylottosimu
pylupdate4 complete.pro
```

translate your language file: lotto1_xx.ts, and produce the .ts translation files with

`lrelease complete.pro`

![Image](misc/pyLottoSimu_screenshot_en.png "screenshot")

Bedienen
--------

Modus Zufallsgenerator:
Die Zahlen auswählen und mit 'Zufallsgenerator ein' starten

Modus Simulation:
Die Zahlen auswählen und mit 'Start' die Simulation starten.
Dabei kann mit dem Schieber oben links die Geschwindigkeit verändert werden.

![Image](misc/pyLottoSimu_screenshot_de.png "screenshot (german)")

License
-------

GNU GPL V3
