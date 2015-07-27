# -*- coding: utf-8 -*-

"""
pyLottoSimu

Copyright (C) <2015> Markus Hackspacher

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

import unittest
from pprint import pprint
from lottosystem import lottosystemdata


class TestCodeFormat(unittest.TestCase):

    def setUp(self):
        self.lottosystem =lottosystemdata()

    def test_readfile(self):
        data = self.lottosystem.readfile()
        fixdata = self.lottosystem.fixdata()
        print data[0]['name']
        self.assertEqual(data[0]['name'], fixdata[0]['name'])

if __name__ == '__main__':
    unittest.main()
