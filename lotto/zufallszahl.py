#!/usr/bin/python
# -*- coding: utf-8 -*-
 
__rev_id__ = """$Id: zufallszahl.py,v 0.1 2010/11/2 Markus Hackspacher cc by-sa $"""

from random import randint
import math
 
# Zufallszahl ermitteln und als Wuerfelergebnis nehmen. 
def zufallszahlen(anzahl,maxwert):
  """
  >>> zufallszahlen(16,15)  
  Traceback (most recent call last):
  ValueError: Anzahl ist größer als der Maximalwert
  >>> zufallszahlen(1,1)
  [1]
  >>> zufallszahlen(1,1.7)
  Traceback (most recent call last):
  ValueError: Keine Gleitkommazahlen!
  >>> sorted(zufallszahlen(3,3))
  [1, 2, 3]
  """
  if anzahl > maxwert:
        raise ValueError("Anzahl ist größer als der Maximalwert")
  if anzahl < 0: 
        raise ValueError("Keine negativen Zahlen!")

  if math.floor(maxwert) != maxwert: 
        raise ValueError("Keine Gleitkommazahlen!")
        return


  wuerfel = []
  i=1
  while i<=anzahl:
    wurf=randint(1, maxwert)
    if not wuerfel.count(wurf):
      wuerfel.append(wurf)
      i+=1
  #wuerfel.sort()
  return (wuerfel)
  
if __name__ == "__main__":
  import doctest
  doctest.testmod()
  print "zufallszahlen(6,49):",zufallszahlen(6,49)
  print sorted(zufallszahlen(3,3))
  a=zufallszahlen(3,30)
  print a,a[:-1],a[-1]