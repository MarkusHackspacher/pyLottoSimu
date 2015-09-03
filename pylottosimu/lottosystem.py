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

import json


class lottosystemdata():
    """
    Read and write the data set of the lottosystem
    """
    def __init__(self):
        try:
            self.data = self.readfile()
        except:
            self.data = self.fixdata()

    def writetofile(self):
        with open('lottosystems.json', 'w') as outfile:
            json.dump(self.data, outfile, sort_keys=True,
                      indent=4, separators=(',', ': '))

    def readfile(self):
        """read lottosystems.json

        :returns: data"""
        with open('lottosystems.json') as data_file:
            data = json.load(data_file)
        return data

    def fixdata(self):
        """read fix data set of the lottosystem

        :returns: data"""
        data = [{
            'name': 'Lotto DE',
            'max_draw': 49,
            'draw_numbers': 6,
            'with_addit': False,
            'addit_numbers': 0,
            'sep_addit_numbers': False,
            'max_addit': 0},
            {
            'name': 'Lotto AT',
            'max_draw': 45,
            'draw_numbers': 6,
            'with_addit': True,
            'addit_numbers': 1,
            'sep_addit_numbers': False,
            'max_addit': 0},
            {
            'name': 'EuroMillionen',
            'max_draw': 50,
            'draw_numbers': 5,
            'with_addit': True,
            'addit_numbers': 2,
            'sep_addit_numbers': True,
            'max_addit': 11},
            {
            'name': 'Powerball Lottery US',
            'max_draw': 59,
            'draw_numbers': 5,
            'with_addit': True,
            'addit_numbers': 1,
            'sep_addit_numbers': True,
            'max_addit': 35
            }]
        return data
