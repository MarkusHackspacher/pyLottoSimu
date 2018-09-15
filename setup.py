#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyLottoSimu, load module lotto

# Copyright (C) <2014-2018> Markus Hackspacher

# This file is part of pyLottoSimu.

# pyLottoSimu is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pyLottoSimu is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pyLottoSimu.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

import py2exe

setup(name='pyLottoSimu',
      version='1.8',
      description='Python Lotto Simulator',
      author='Markus Hackspacher',
      author_email='hackspacher@gmx.de',
      url='http://pylottosimu.readthedocs.org',
      download_url='https://github.com/MarkusHackspacher/pyLottoSimu',
      packages=['pylottosimu'],
      data_files=[('pylottosimu', ["pylottosimu/lottosimu_gui.ui",
                                   "pylottosimu/lottokugel.svg"]),
                  ('pylottosimu/dialog',
                   ["pylottosimu/dialog/lottosystem.ui"]),
                  ('misc', ["misc/pyLottoSimu.svg"]),
                  ('pylottosimu/translation',
                   ["pylottosimu/translation/lotto1_de.qm",
                    "pylottosimu/translation/lotto1_dk.qm",
                    "pylottosimu/translation/lotto1_es.qm",
                    "pylottosimu/translation/lotto1_fr.qm",
                    "pylottosimu/translation/lotto1_it.qm",
                    "pylottosimu/translation/lotto1_nl.qm",
                    "pylottosimu/translation/lotto1_pl.qm",
                    "pylottosimu/translation/lotto1_ru.qm"])],
      license='GPLv3',
      # windows=['pylottosimu.pyw'],
      console=['lotto.pyw'],
      options={"py2exe": {"dll_excludes": ["MSVCP90.dll", "HID.DLL",
                                           "w9xpopen.exe"],
                          "includes": ["sip", ],
                          'bundle_files': 1,
                          "optimize": 2}, },
      )
