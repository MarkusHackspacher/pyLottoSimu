.. pyLottoSimu documentation master file, created by
   sphinx-quickstart on Sun Aug 23 23:13:31 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyLottoSimu's documentation!
=======================================

Lotto Generator and Simulator

a simulation of Lotto Germany (pick 6 out of 49), Lotto Austria (pick 6 out of 45), EuroMillionen,
Powerball Lottery US, Mega Millions lottery and Hot Lotto Sizzler system.

The pyLottoSimu program generates random lottery numbers and can
simulate a draw. In the simulation view a Lotto Ball is visible on the
numbers rotate faster and faster, and is finally available, this is the
text, the first number of today\'s draw was the ... Maybe it was indeed
actually the numbers of the next draw, of course are here, all the
figures provided without guarantee.

pyLottoSimu can be started in these languages:

English, German, French, Spanish, Italian, Danish, Dutch, Polish and Russian

Start
-----

The program requires Python_ 2.7 or 3.x and `Qt5 for Python`_.

.. _Python: http://www.python.org/download/
.. _Qt5 for Python: http://www.riverbankcomputing.com/software/pyqt/download5

Start with::

  python lotto.pyw [de|dk|fr|es|it|nl|pl|ru]

Documentation
-------------

Make the documentation as .html file::

  cd docs
  make html

Add new modules with::

  cd docs
  sphinx-apidoc -f -o . ../pylottosimu
  
.. image:: ../misc/pyLottoSimu_screenshot_en.png


Contents:

.. toctree::
   :maxdepth: 2

   install
   translate
   history
   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

