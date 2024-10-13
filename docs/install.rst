Installation
============

Installing pyLottoSimu should usually be quite easy, as you can simply unpack
and run pyLottoSimu in place if you wish to do so.

.. contents::


dependencies
------------

You'll need these dependencies to run the program:

 * `python <http://www.python.org>`_ - The python programming language along with python-setuptools
 * `PyQt6 <http://www.riverbankcomputing.com/software/pyqt/download5>`_ - Qt5 for Python

build the help

 * `Sphinx <http://sphinx-doc.org/>`_ - Documentation

code test

 * pycodestyle - Python style guide checker
 * isort - import sorting and checking tool
 * nose - start nosetests to run the tests

version control system Git

 * `Git <https://git-scm.com/>`_ - Git - distributed version control system


Installing Debian or Ubuntu
---------------------------

First you need to your computer these programs: Python, PyQt6 and version control system git::

    # sudo apt-get install python python-PyQt6 python-PyQt6.qtsvg git
    # sudo apt-get install python3 python3-PyQt6 python3-PyQt6.qtsvg git

Then you copied the source code of the program on your computer,
either download the zip file of the project or download with the version control system::

    # git clone https://github.com/MarkusHackspacher/pyLottoSimu.git

change the directory and run::

    cd pyLottoSimu
    ./lotto.pyw

alternative::

    python lotto.pyw [de|dk|fr|es|it|nl|pl|ru]
    python3 lotto.pyw [de|dk|fr|es|it|nl|pl|ru]


