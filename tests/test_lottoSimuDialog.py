# -*- coding: utf-8 -*-

# pyLottoSimu

# Copyright (C) <2015-2018> Markus Hackspacher

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

"""Test the dialog module LottoSimuDialog
"""

from unittest import TestCase

from PyQt5 import QtWidgets

from pylottosimu.pylotto import LottoSimuDialog


class TestLottoSimuDialog(TestCase):
    def setUp(self):
        """Creates the QApplication instance"""

        # Simple way of making instance a singleton
        super(TestLottoSimuDialog, self).setUp()
        self.app = QtWidgets.QApplication([])

        self.ui = LottoSimuDialog()

    def tearDown(self):
        """Deletes the reference owned by self"""
        del self.app
        super(TestLottoSimuDialog, self).tearDown()

    def test_onInfo(self):
        self.ui.onInfo(True)