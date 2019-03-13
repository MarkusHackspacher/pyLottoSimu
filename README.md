pyLottoSimu
===========

[![Build Status](https://travis-ci.org/MarkusHackspacher/pyLottoSimu.svg?branch=master)](https://travis-ci.org/MarkusHackspacher/pyLottoSimu)
[![Github Releases](https://img.shields.io/github/release/markushackspacher/pylottosimu.svg)](https://github.com/MarkusHackspacher/pyLottoSimu)
[![Join the chat at https://gitter.im/MarkusHackspacher/pyLottoSimu](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/MarkusHackspacher/pyLottoSimu?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Documentation Status](https://readthedocs.org/projects/pylottosimu/badge/?version=latest)](https://readthedocs.org/projects/pylottosimu/?badge=latest)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6b96ee1e2b2d415ca10677b604990cd9)](https://www.codacy.com/app/MarkusHackspacher/pyLottoSimu?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=MarkusHackspacher/pyLottoSimu&amp;utm_campaign=Badge_Grade)
[![Crowdin](https://d322cqt584bo4o.cloudfront.net/pylottosimu/localized.svg)](https://crowdin.com/project/pylottosimu)

a Lotto Generator und Simulator

a simulation of Lotto Germany (pick 6 out of 49), Lotto Austria (pick 6 out of 45), EuroMillionen,
Powerball Lottery US, Mega Millions lottery and Hot Lotto Sizzler system.

The program is developed on [github.com/MarkusHackspacher/pyLottoSimu](https://github.com/MarkusHackspacher/pyLottoSimu).
Feedback and contributions are welcome.

Help to translate with https://crowdin.com/project/pylottosimu
Login with Github possible.

install
-------

The program requires [Python 3.x](http://www.python.org/download/) 
and PyQt5 for Python 3 `pip3 install PyQt5`.

```
# sudo apt-get install python python-pyqt5 python-pyqt5.qtsvg git
# sudo apt-get install python3 python3-pyqt5 python3-pyqt5.qtsvg git
```
    
Then you copied the source code of the program on your computer,
either [download](https://github.com/MarkusHackspacher/pyLottoSimu) the zip file of the project or download with the version control system:

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
