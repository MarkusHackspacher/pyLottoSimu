# -*- coding: utf-8 -*-

# pyLottoSimu

# Copyright (C) <2015> Markus Hackspacher

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

"""
test the dialog module

show_drawing
"""

import sys
import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
_instance = None

__author__ = 'Markus Hackspacher'
__license__ = "GPL"
__copyright__ = "<2015> Markus Hackspacher"

if sys.version_info >= (3, 0):
    from pylottosimu.dialog.show_drawing import DlgShowDrawing
else:
    from dialog.show_drawing import DlgShowDrawing


class show_drawingTestCase(unittest.TestCase):
    """
    Test of drawing
    """

    def setUp(self):
        '''Creates the QApplication instance'''

        # Simple way of making instance a singleton
        super(show_drawingTestCase, self).setUp()
        global _instance
        if _instance is None:
            _instance = QApplication([])

        self.app = _instance

    def tearDown(self):
        '''Deletes the reference owned by self'''
        del self.app
        super(show_drawingTestCase, self).tearDown()

    def test_setting(self):
        '''settings'''
        dialog = DlgShowDrawing([3, 4], 6)
        self.assertTrue(dialog)
        self.assertEqual(dialog.btn_drawnumbers[0].text(), '1')
        self.assertEqual(dialog.btn_drawnumbers[0].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[1].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[2].isFlat(), False)
        self.assertEqual(dialog.btn_drawnumbers[3].isFlat(), False)
        self.assertEqual(dialog.btn_drawnumbers[4].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[5].isFlat(), True)

    def test_ballnumbers(self):
        '''test ballnumbers'''
        dialog = DlgShowDrawing([2], 5)
        self.assertTrue(dialog)

    def test_bonusnumbers(self):
        '''test bonusnumbers'''
        dialog = DlgShowDrawing([2], 5, [1])
        self.assertTrue(dialog)

    def test_bonusnumbersseparate(self):
        '''test separate bonusnumbers'''
        dialog = DlgShowDrawing([2], 5, [1, 2], 2)
        self.assertTrue(dialog)

if __name__ == '__main__':
    unittest.main()
