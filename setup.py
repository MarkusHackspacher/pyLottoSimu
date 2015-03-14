#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyLottoSimu, load module lotto

Copyright (C) <2014> Markus Hackspacher

This file is part of pyLottoSimu.

pyLottoSimu is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyLottoSimu is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyLottoSimu.  If not, see <http://www.gnu.org/licenses/>.
"""
from py2exe.build_exe import py2exe
from distutils.core import setup


setup(name='pyLottoSimu',
      version='1.5',
      description='Python Lotto Simulator',
      author='Markus Hackspacher',
      author_email='hackspacher@gmx.de',
      url='http://markush.cwsurf.de/joomla_17/index.php/python/pylottosimu',
      download_url='https://github.com/MarkusHackspacher/pyLottoSimu',
      packages=['pylottosimu', 'pylottosimu.dialog'],
      license='GPL',
      console=["pylottosimu.pyw"],
      options={"py2exe": {"dll_excludes": ["MSVCP90.dll", "HID.DLL",
                                           "w9xpopen.exe"],
                          "includes": ["sip", ]}, },
      )
