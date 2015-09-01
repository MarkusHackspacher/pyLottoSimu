.. pyLottoSimu documentation master file, created by
   sphinx-quickstart on Sun Aug 23 23:13:31 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyLottoSimu's documentation!
=======================================

Lotto Generator and Simulator

a simulation of the German (6 of 49), Austria (6 of 45)
or EuroMillionen (5 of 50 plus 2) lottery system.

The pyLottoSimu program generates random lottery numbers and can
simulate a draw. In the simulation view a Lotto Ball is visible on the
numbers rotate faster and faster, and is finally available, this is the
text, the first number of today\'s draw was the ... Maybe it was indeed
actually the numbers of the next draw, of course are here, all the
figures provided without guarantee.

Start
-----

The program requires Python_ 2.7 or 3.x and `Qt5 for Python`_.

.. _Python: http://www.python.org/download/
.. _Qt5 for Python: http://www.riverbankcomputing.com/software/pyqt/download5

Start with::

  python lotto.pyw [de|fr|es|it|ru]

Documentation
-------------

Make the documentation as .html file::

  cd docs
  make html

Translate
---------

To translate the program or make a translation in your language,
insert in the complete.pro your language code.
::

  cd pylottosimu
  pylupdate4 complete.pro

translate your language file: lotto1_xx.ts, and produce the .ts translation files with::

  lrelease complete.pro

.. image:: ../misc/pyLottoSimu_screenshot_en.png


Contents:

.. toctree::
   :maxdepth: 2

   modules
   code

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

