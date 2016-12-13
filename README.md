pyLottoSimu
===========

[![Github Releases](https://img.shields.io/github/release/markushackspacher/pylottosimu.svg)](https://github.com/MarkusHackspacher/pyLottoSimu)
[![Join the chat at https://gitter.im/MarkusHackspacher/pyLottoSimu](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/MarkusHackspacher/pyLottoSimu?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Documentation Status](https://readthedocs.org/projects/pylottosimu/badge/?version=latest)](https://readthedocs.org/projects/pylottosimu/?badge=latest)

Lotto Generator und Simulator

a simulation of Lotto Germany (pick 6 out of 49), Lotto Austria (pick 6 out of 45), EuroMillionen,
Powerball Lottery US, Mega Millions lottery and Hot Lotto Sizzler system.

test                 | result
---------------------|--------
**Python 2 + pyQt4** | [![Build Status](https://drone.io/github.com/MarkusHackspacher/pyLottoSimu/status.png)](https://drone.io/github.com/MarkusHackspacher/pyLottoSimu/latest)
**Python 3 + PyQt5** | [![Build Status](https://travis-ci.org/MarkusHackspacher/pyLottoSimu.svg?branch=master)](https://travis-ci.org/MarkusHackspacher/pyLottoSimu)


install
-------

The program requires [Python 2.7 or 3.x](http://www.python.org/download/) 
and [PyQt4 for Python 2](http://www.riverbankcomputing.com/software/pyqt/download)
or PyQt5 for Python 3 `pip3 install PyQt5`.

```
# sudo apt-get install python python-pyqt5 python-pyqt5.qtsvg git
# sudo apt-get install python3 python3-pyqt5 python3-pyqt5.qtsvg git
```
    
Then you copied the source code of the program on your computer,
either download the zip file of the project or download with the version control system::

```
# git clone https://github.com/MarkusHackspacher/pyLottoSimu.git
```

change the directory and run::

```
cd pyLottoSimu
./lotto.pyw
```

pyLottoSimu can be started in these languages:

English, German, French, Spanish, Italian, Danish, Dutch, Polish and Russian

Start with:

`python lotto.pyw [de|dk|fr|es|it|nl|pl|ru]`

Make the documentation as .html file:

```
cd docs
make html
```

To translate the program or make a translation in your language
insert in the complete.pro your language code.


```
cd pylottosimu
pylupdate4 complete.pro
```

Translate your language file or fix a typo in the lotto1_xx.ts file.
Produce the .ts translation files with:

`lrelease complete.pro`

feel free and send me a pull request. Thank you in advance.

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
