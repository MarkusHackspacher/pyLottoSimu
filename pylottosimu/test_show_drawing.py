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
from __future__ import absolute_import

import unittest
from pylottosimu.dialog.show_drawing import DlgShowDrawing

_FORCE_PYSIDE = False
_FORCE_PYQT4 = False

try:
    if _FORCE_PYSIDE or _FORCE_PYQT4:
        raise ImportError('_FORCE_PYSIDE')
    from PyQt5 import QtWidgets
except ImportError:
    try:
        if _FORCE_PYQT4:
            raise ImportError('_FORCE_PYSIDE')
        from PySide import QtGui as QtWidgets
    except ImportError:
        from PyQt4 import QtGui as QtWidgets

_instance = None

__author__ = 'Markus Hackspacher'
__license__ = "GPL"
__copyright__ = "<2015> Markus Hackspacher"


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
            _instance = QtWidgets.QApplication([])

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
