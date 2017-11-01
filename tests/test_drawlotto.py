# -*- coding: utf-8 -*-

# pyLottoSimu

# Copyright (C) <2015-2017> Markus Hackspacher

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

from __future__ import unicode_literals

import unittest

from pylottosimu import pylotto


class DrawLottoTestCase(unittest.TestCase):
    """Test the lotto draw with some input numbers
    """
    def setUp(self):
        """Init class pylotto.drawlotto

        :return: none
        """
        self.lotto = pylotto.DrawLotto(with_addit=False, addit_numbers=2,
                                       sep_addit_numbers=True, max_addit=10)

    def test_setting(self):
        """Test lotto.data

        :return: none
        """
        self.assertEqual(self.lotto.data['name'], 'Lotto DE')
        self.assertEqual(self.lotto.data['max_draw'], 49)
        self.assertEqual(self.lotto.data['draw_numbers'], 6)
        self.assertEqual(self.lotto.data['with_addit'], False)
        self.assertEqual(self.lotto.data['addit_numbers'], 2)
        self.assertEqual(self.lotto.data['sep_addit_numbers'], True)
        self.assertEqual(self.lotto.data['max_addit'], 10)

    def test_draw(self):
        """test draw without a additional number

        :return: none
        """
        self.lotto.data['with_addit'] = False
        self.lotto.draw()
        self.assertEqual(len(self.lotto.random_number), 6)
        self.assertEqual(len(self.lotto.random_addit), 0)
        self.assertEqual(len(self.lotto.ballnumber), 6)
        self.assertEqual(len(self.lotto.ballbonus), 0)
        self.assertEqual(self.lotto.picknumber(-1)[:28],
                         'Welcome to the lottery draw,')
        self.assertEqual(self.lotto.picknumber(0)[:35],
                         'And the first winning number is the')

    def test_draw_addit(self):
        """test draw with a additional number

        :return: none
        """
        self.lotto.data['with_addit'] = True
        self.lotto.data['sep_addit_numbers'] = False
        self.lotto.draw()
        self.assertEqual(len(self.lotto.random_number), 8)
        self.assertEqual(len(self.lotto.random_addit), 0)
        self.assertEqual(len(self.lotto.ballnumber), 6)
        self.assertEqual(len(self.lotto.ballbonus), 2)
        self.assertEqual(self.lotto.picknumber(-1)[:28],
                         'Welcome to the lottery draw,')
        self.assertEqual(self.lotto.picknumber(0)[:35],
                         'And the first winning number is the')

    def test_draw_addit_sep(self):
        """test draw with a separate additional number

        :return: none
        """
        self.lotto.data['with_addit'] = True
        self.lotto.data['sep_addit_numbers'] = True
        self.lotto.draw()
        self.assertEqual(len(self.lotto.random_number), 6)
        self.assertEqual(len(self.lotto.random_addit), 2)
        self.assertEqual(len(self.lotto.ballnumber), 6)
        self.assertEqual(len(self.lotto.ballbonus), 2)
        self.assertEqual(self.lotto.picknumber(-1)[:28],
                         'Welcome to the lottery draw,')
        self.assertEqual(self.lotto.picknumber(0)[:35],
                         'And the first winning number is the')

    def test_drawone(self):
        """test draw one number without a additional number

        :return: none
        """
        self.lotto.data['draw_numbers'] = 1
        self.lotto.data['with_addit'] = False
        self.assertEqual(self.lotto.data['draw_numbers'], 1)
        self.lotto.draw()
        self.assertEqual(len(self.lotto.random_number), 1)
        self.assertEqual(len(self.lotto.random_addit), 0)
        self.assertEqual(len(self.lotto.ballnumber), 1)
        self.assertEqual(len(self.lotto.ballbonus), 0)
        self.assertEqual(self.lotto.picknumber(-1)[:28],
                         'Welcome to the lottery draw,')
        self.assertEqual(self.lotto.picknumber(0)[:22],

                         'And now we come to the')

    def test_drawtwo(self):
        """test draw two number without a additional number

        :return: none
        """
        self.lotto.data['draw_numbers'] = 2
        self.lotto.data['with_addit'] = False
        self.assertEqual(self.lotto.data['draw_numbers'], 2)
        self.lotto.draw()
        self.assertEqual(len(self.lotto.random_number), 2)
        self.assertEqual(len(self.lotto.random_addit), 0)
        self.assertEqual(len(self.lotto.ballnumber), 2)
        self.assertEqual(len(self.lotto.ballbonus), 0)
        self.assertEqual(self.lotto.picknumber(-1)[:28],
                         'Welcome to the lottery draw,')
        self.assertEqual(self.lotto.picknumber(0)[:35],
                         'And the first winning number is the')
        self.assertEqual(self.lotto.picknumber(1)[:22],
                         'And now we come to the')

    def test_drawthree(self):
        """test draw three number without a additional number

        :return: none
        """
        self.lotto.data['draw_numbers'] = 3
        self.lotto.data['with_addit'] = False
        self.assertEqual(self.lotto.data['draw_numbers'], 3)
        self.lotto.draw()
        self.assertEqual(len(self.lotto.random_number), 3)
        self.assertEqual(len(self.lotto.random_addit), 0)
        self.assertEqual(len(self.lotto.ballnumber), 3)
        self.assertEqual(len(self.lotto.ballbonus), 0)
        self.assertEqual(self.lotto.picknumber(-1)[:28],
                         'Welcome to the lottery draw,')
        self.assertEqual(self.lotto.picknumber(0)[:35],
                         'And the first winning number is the')
        self.assertEqual(self.lotto.picknumber(1)[:36],
                         'We are already at the winning number')
        self.assertEqual(self.lotto.picknumber(2)[:22],
                         'And now we come to the')

    def test_drawzero(self):
        """test set draw to no number and make sure to set to one number

        :return: none
        """
        self.lotto.data['draw_numbers'] = 0
        self.lotto.data['with_addit'] = False
        self.assertEqual(self.lotto.data['draw_numbers'], 0)
        self.lotto.draw()
        self.assertEqual(len(self.lotto.random_number), 1)
        self.assertEqual(self.lotto.picknumber(0)[:22],
                         'And now we come to the')


if __name__ == '__main__':
    unittest.main()
