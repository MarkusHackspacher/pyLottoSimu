#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Erzeugen einer Zufallszahl, mit Modultest beim direkten Aufruf

pyLottoSimu

Copyright (C) <2012-2014> Markus Hackspacher

This file is part of pyLottoverwaltung.

pyLottoverwaltung is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyLottoverwaltung is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyLottoverwaltung.  If not, see <http://www.gnu.org/licenses/>.
"""


import random


def zufallszahlen(anzahl, maxwert):
    """
    Zufallszahl ermitteln und als Wuerfelergebnis nehmen
    return random valve
    @param anzahl: Gibt die Anzahl der Ausgabewerte an
    @param maxwert: Gibt den höchsten Zahlenwert an
    @type anzahl: int
    @type maxwert: int
    @return: Gibt Zufallszahlen zurueck.
    
    >>> zufallszahlen(16, 15)
    Traceback (most recent call last):
    ValueError: Sample larger than population
    >>> zufallszahlen(16, -15)
    Traceback (most recent call last):
    ValueError: Sample larger than population
    >>> zufallszahlen(-16, 15)
    Traceback (most recent call last):
    ValueError: Sample larger than population
    >>> zufallszahlen(1, 1)
    [1]
    >>> zufallszahlen(1, 1.7)
    Traceback (most recent call last):
    TypeError: 'float' object cannot be interpreted as an integer
    >>> sorted(zufallszahlen(3, 3))
    [1, 2, 3]
    """
    return random.sample(range(1, maxwert + 1), anzahl)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print ("zufallszahlen(6, 49):", zufallszahlen(6, 49))
    print (sorted(zufallszahlen(3, 3)))
    a = zufallszahlen(3, 30)
    print (a, a[:-1], a[-1])
