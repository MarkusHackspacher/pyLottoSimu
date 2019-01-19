# -*- coding: utf-8 -*-

# pyLottoSimu

# Copyright (C) <2015-2019> Markus Hackspacher

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

"""Test the dialog module

lottosettingdialog
"""
import unittest

from PyQt5 import QtWidgets

from pylottosimu.dialog.lottosettingdialog import LottoSettingsDialog
from pylottosimu.lottosystem import LottoSystemData


class LottoSystemDataTestCase(unittest.TestCase):
    """Test of drawing
    """

    def setUp(self):
        """Creates the QApplication instance

        :return: none
        """

        # Simple way of making instance a singleton
        super(LottoSystemDataTestCase, self).setUp()

        self.app = QtWidgets.QApplication([])

    def tearDown(self):
        """Deletes the reference owned by self

        :return: none
        """
        del self.app
        super(LottoSystemDataTestCase, self).tearDown()

    def test_dialog(self):
        """test"""
        lottosystems = LottoSystemData()
        dialog = LottoSettingsDialog(lottosystems, testcase=True)
        self.assertTrue(dialog)

    def test_dialogvalues(self):
        """test"""
        lottosystems = LottoSystemData()
        dialog = LottoSettingsDialog(lottosystems, testcase=True)
        self.assertEqual(
            dialog.values(),
            ('Lotto DE', 49, 6, False, 0, False, 0, 'Superzahl'))


if __name__ == '__main__':
    unittest.main()
