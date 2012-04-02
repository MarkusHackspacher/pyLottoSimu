#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Erzeugen einer Zufallszahl mit Modultest beim direkten Aufruf
"""

import random
 
# Zufallszahl ermitteln und als Wuerfelergebnis nehmen. 
def zufallszahlen(anzahl,maxwert):
    """
    >>> zufallszahlen(16, 15)  
    Traceback (most recent call last):
    ValueError: sample larger than population
    >>> zufallszahlen(16, -15)  
    Traceback (most recent call last):
    ValueError: sample larger than population
    >>> zufallszahlen(-16, 15)  
    Traceback (most recent call last):
    ValueError: sample larger than population
    >>> zufallszahlen(1, 1)
    [1]
    >>> zufallszahlen(1, 1.7)
    Traceback (most recent call last):
    TypeError: integer argument expected, got float
    >>> sorted(zufallszahlen(3, 3))
    [1, 2, 3]
    """
    return random.sample(xrange(1, maxwert + 1), anzahl)
  
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print "zufallszahlen(6, 49):",zufallszahlen(6, 49)
    print sorted(zufallszahlen(3, 3))
    a=zufallszahlen(3, 30)
    print a, a[:-1], a[-1]