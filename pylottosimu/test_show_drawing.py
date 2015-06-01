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

import sys
import unittest
from PyQt4.QtGui import QApplication
from PyQt4.QtTest import QTest
from PyQt4.QtCore import Qt
_instance = None


if sys.version_info >= (3, 0):
    from pylottosimu.dialog.show_drawing import DlgShowDrawing
else:
    from dialog.show_drawing import DlgShowDrawing

__author__ = 'mar'


class show_drawingTestCase(unittest.TestCase):

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
        dialog = DlgShowDrawing([3, 4], 6)
        self.assertTrue(dialog)
        self.assertEqual(dialog.Btn_Numerary_1to49[0].text(), '1')
        self.assertEqual(dialog.Btn_Numerary_1to49[0].isFlat(), True)
        self.assertEqual(dialog.Btn_Numerary_1to49[1].isFlat(), True)
        self.assertEqual(dialog.Btn_Numerary_1to49[2].isFlat(), False)
        self.assertEqual(dialog.Btn_Numerary_1to49[3].isFlat(), False)
        self.assertEqual(dialog.Btn_Numerary_1to49[4].isFlat(), True)
        self.assertEqual(dialog.Btn_Numerary_1to49[5].isFlat(), True)

    def test_ballnumbers(self):
        dialog = DlgShowDrawing([2], 5)
        self.assertTrue(dialog)

    def test_bonusnumbers(self):
        dialog = DlgShowDrawing([2], 5, [1])
        self.assertTrue(dialog)

    def test_bonusnumbersseparate(self):
        dialog = DlgShowDrawing([2], 5, [1, 2], 2)
        self.assertTrue(dialog)

if __name__ == '__main__':
    unittest.main()
