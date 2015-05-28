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

import pylotto


class drawlottoTestCase(unittest.TestCase):
    def setUp(self):
        self.lotto = pylotto.drawlotto(with_addit=False, addit_numbers=2,
                                       sep_addit_numbers=True, max_addit=10)

    def test_setting(self):
        self.assertEqual(self.lotto.data['name'], 'Lotto DE')
        self.assertEqual(self.lotto.data['max_draw'], 49)
        self.assertEqual(self.lotto.data['draw_numbers'], 6)
        self.assertEqual(self.lotto.data['with_addit'], False)
        self.assertEqual(self.lotto.data['addit_numbers'], 2)
        self.assertEqual(self.lotto.data['sep_addit_numbers'], True)
        self.assertEqual(self.lotto.data['max_addit'], 10)

    def test_draw(self):
        self.lotto.data['with_addit'] = False
        self.lotto.draw()
        self.assertEqual(len(self.lotto.random_number), 6)
        self.assertEqual(len(self.lotto.random_addit), 0)

    def test_draw_addit(self):
        self.lotto.data['with_addit'] = True
        self.lotto.data['sep_addit_numbers'] = False
        self.lotto.draw()
        self.assertEqual(len(self.lotto.random_number), 8)
        self.assertEqual(len(self.lotto.random_addit), 0)

    def test_draw_addit_sep(self):
        self.lotto.data['with_addit'] = True
        self.lotto.data['sep_addit_numbers'] = True
        self.lotto.draw()
        self.assertEqual(len(self.lotto.random_number), 6)
        self.assertEqual(len(self.lotto.random_addit), 2)

if __name__ == '__main__':
    unittest.main()
