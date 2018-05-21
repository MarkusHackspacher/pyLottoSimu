#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyLottoSimu

# Copyright (C) <2012-2018> Markus Hackspacher

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

import json
import os


class LottoSystemData(object):
    """
    loads predefined lottery systems.
    And read and write a json file of the data set.

    Dataset:

    - name: name of the lottery system,
    - max_draw: highest number of draw
    - draw_numbers: number to pick
    - with_addit: with additional number
    - sep_addit_numbers: with separate additional number,
      the additional number are not in the same pot
    - addit_numbers: additional number to pick
    - max_addit: highest additional number in the separate pot

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

    @staticmethod
    def fixdata():
        """Data of predefined lottery system.

        The following are predefined:
        Lotto Germany (pick 6 out of 49),
        Lotto Austria (pick 6 out of 45),
        EuroMillionen,
        Powerball Lottery US,
        Mega Millions,
        Hot Lotto Sizzler

        If you miss your favorite lottery system than could you add here.

        :returns: data"""
        data = [
            {
                'name': 'Lotto DE',
                'max_draw': 49,
                'draw_numbers': 6,
                'with_addition': False,
                'addition_numbers': 0,
                'sep_addition_numbers': False,
                'max_addition': 0,
                'name_addition': 'Superzahl'
            },
            {
                'name': 'Lotto AT',
                'max_draw': 45,
                'draw_numbers': 6,
                'with_addition': True,
                'addition_numbers': 1,
                'sep_addition_numbers': False,
                'max_addition': 0,
                'name_addition': ''
            },
            {
                'name': 'EuroMillionen',
                'max_draw': 50,
                'draw_numbers': 5,
                'with_addition': True,
                'addition_numbers': 2,
                'sep_addition_numbers': True,
                'max_addition': 11,
                'name_addition': ''
            },
            {
                'name': 'Powerball Lottery US',
                'max_draw': 59,
                'draw_numbers': 5,
                'with_addition': True,
                'addition_numbers': 1,
                'sep_addition_numbers': True,
                'max_addition': 35,
                'name_addition': ''
            },
            {
                "name": "Mega Millions",
                "max_draw": 56,
                "draw_numbers": 5,
                "addition_numbers": 1,
                "max_addition": 46,
                "sep_addition_numbers": True,
                "with_addition": True,
                'name_addition': ''
            },
            {
                "name": "Hot Lotto Sizzler",
                "max_draw": 19,
                "draw_numbers": 5,
                "addition_numbers": 1,
                "max_addition": 47,
                "sep_addition_numbers": True,
                "with_addition": True,
                'name_addition': ''
            }
        ]
        return data
