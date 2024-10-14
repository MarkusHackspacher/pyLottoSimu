# -*- coding: utf-8 -*-

# pyLottoSimu

# Copyright (C) <2015-2024> Markus Hackspacher

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

LottoSimuDialog
"""

from unittest import TestCase

try:
    from PyQt6.QtWidgets import QApplication
except ImportError:
    from PyQt5.QtWidgets import QApplication

from pylottosimu.pylotto import LottoSimuDialog


class TestLottoSimuDialog(TestCase):
    def setUp(self):
        """Creates the QApplication instance"""

        # Simple way of making instance a singleton
        super(TestLottoSimuDialog, self).setUp()
        self.app = QApplication([])

        self.ui = LottoSimuDialog()

    def tearDown(self):
        """Deletes the reference owned by self"""
        del self.app
        super(TestLottoSimuDialog, self).tearDown()

    def test_onInfo(self):
        self.ui.onInfo(True)

    def test_showNextNumber(self):
        self.ui.turn = 0
        self.assertEqual(self.ui.lottodraw.random_number, [])
        self.assertEqual(self.ui.lottodraw.random_addit, [])
        self.ui.lottodraw.random_number = [1]
        self.ui.showNextNumber()
        self.assertEqual(self.ui.ui.plaintextedit.toPlainText(),
                         'And the first winning number is the 1.')
