#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyLottoSimu

# Copyright (C) <2012-2015> Markus Hackspacher

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

import os
import sys
import json


class lottosystemdata():
    """
    The class lottosystemdata loads predefined lotto systems.
    And read and write a json file of the data set.

    .. todo:: at program start: look for the right path in the home environ
     load json and last use lotto

    .. todo:: if not exits: save the json file in the home

    .. todo:: program exit: save the last use lotto system

    """
    def __init__(self):
        self.dirname = ''
        # try:
        # self.data = self.readfile()
        # except:
        self.data = self.fixdata()

    def projectpath(self):
        """ open in the home path and create a direction.

        :returns: path of the project
        """
        path = os.environ['HOME']
        if os.path.exists(path):
            dirname = os.path.join(self.path, '.pylottosimu')
            if not os.path.exists(dirname):
                os.mkdir(dirname)
        return dirname

    def writetofile(self):
        """write lottosystems.json

        :returns: none"""
        with open(os.path.join(
                self.dirname, 'lottosystems.json'), 'w') as outfile:
            json.dump(self.data, outfile, sort_keys=True,
                      indent=4, separators=(',', ': '))

    def readfile(self):
        """read lottosystems.json

        :returns: data"""
        with open(os.path.join(
                self.dirname, 'lottosystems.json')) as data_file:
            data = json.load(data_file)
        return data

    def fixdata(self):
        """Returns predefined lottosystems.
        the following are predefined:
        Lotto Germany, 6 from 49
        Lotto Austria, 6 from 45
        EuroMillionen, 5 from 50
        Powerball Lottery US, 5 from 59
        Mega Millions

        :returns: data"""
        data = [
            {
                'name': 'Lotto DE',
                'max_draw': 49,
                'draw_numbers': 6,
                'with_addit': False,
                'addit_numbers': 0,
                'sep_addit_numbers': False,
                'max_addit': 0
            },
            {
                'name': 'Lotto AT',
                'max_draw': 45,
                'draw_numbers': 6,
                'with_addit': True,
                'addit_numbers': 1,
                'sep_addit_numbers': False,
                'max_addit': 0
            },
            {
                'name': 'EuroMillionen',
                'max_draw': 50,
                'draw_numbers': 5,
                'with_addit': True,
                'addit_numbers': 2,
                'sep_addit_numbers': True,
                'max_addit': 11
            },
            {
                'name': 'Powerball Lottery US',
                'max_draw': 59,
                'draw_numbers': 5,
                'with_addit': True,
                'addit_numbers': 1,
                'sep_addit_numbers': True,
                'max_addit': 35},
            {
                "name": "Mega Millions",
                "max_draw": 56,
                "draw_numbers": 5,
                "addit_numbers": 1,
                "max_addit": 46,
                "sep_addit_numbers": True,
                "with_addit": True
            },
            {
                "name": "Hot Lotto Sizzler",
                "max_draw": 19,
                "draw_numbers": 5,
                "addit_numbers": 1,
                "max_addit": 47,
                "sep_addit_numbers": True,
                "with_addit": True
            }
        ]
        return data
