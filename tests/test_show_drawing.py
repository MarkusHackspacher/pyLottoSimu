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

"""Test the dialog module show_drawing
"""

import unittest

from PyQt5 import QtWidgets

from pylottosimu.dialog.show_drawing import DlgShowDrawing



class ShowDrawingTestCase(unittest.TestCase):
    """
    Test of drawing
    """

    def setUp(self):
        """Creates the QApplication instance"""

        # Simple way of making instance a singleton
        super(ShowDrawingTestCase, self).setUp()

        self.app = QtWidgets.QApplication([])

    def tearDown(self):
        """Deletes the reference owned by self"""
        del self.app
        super(ShowDrawingTestCase, self).tearDown()

    def test_twoballnumber(self):
        """test with two ball numbers"""
        dialog = DlgShowDrawing([3, 4], 6)
        self.assertTrue(dialog)
        self.assertEqual(dialog.btn_drawnumbers[0].text(), '1')
        self.assertEqual(dialog.btn_drawnumbers[0].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[1].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[2].isFlat(), False)
        self.assertEqual(dialog.btn_drawnumbers[3].isFlat(), False)
        self.assertEqual(dialog.btn_drawnumbers[4].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[5].isFlat(), True)

    def test_ballnumber(self):
        """test with one ball numbers"""
        dialog = DlgShowDrawing([2], 5)
        self.assertTrue(dialog)
        self.assertEqual(dialog.btn_drawnumbers[0].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[1].isFlat(), False)
        self.assertEqual(dialog.btn_drawnumbers[2].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[3].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[4].isFlat(), True)

    def test_bonusnumbers(self):
        """test ball numbers and bonus numbers in a maximal draw of 5 numbers
        """
        dialog = DlgShowDrawing([2], 5, [1])
        self.assertTrue(dialog)
        self.assertEqual(dialog.btn_drawnumbers[0].isFlat(), False)
        self.assertEqual(dialog.btn_drawnumbers[0].styleSheet(),
                         'color: blue;')
        self.assertEqual(dialog.btn_drawnumbers[1].isFlat(), False)
        self.assertEqual(dialog.btn_drawnumbers[1].styleSheet(),
                         'color: red;')
        self.assertEqual(dialog.btn_drawnumbers[2].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[2].styleSheet(), '')
        self.assertEqual(dialog.btn_drawnumbers[3].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[4].isFlat(), True)

    def test_samenumbers(self):
        """test the same ball numbers and bonus numbers in a maximal draw
        of 5 numbers

        :return: none
        """
        dialog = DlgShowDrawing([3], 5, [3])
        self.assertTrue(dialog)
        self.assertEqual(dialog.btn_drawnumbers[0].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[0].styleSheet(), '')
        self.assertEqual(dialog.btn_drawnumbers[1].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[1].styleSheet(), '')
        self.assertEqual(dialog.btn_drawnumbers[2].isFlat(), False)
        self.assertEqual(dialog.btn_drawnumbers[2].styleSheet(), 'color: red;')
        self.assertEqual(dialog.btn_drawnumbers[3].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[4].isFlat(), True)

    def test_bonusnumbersseparate(self):
        """test separate bonus numbers

        :return: none
        """
        dialog = DlgShowDrawing([2], 5, [1, 2], 3)
        self.assertTrue(dialog)
        self.assertEqual(dialog.btn_drawnumbers[0].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[1].isFlat(), False)
        self.assertEqual(dialog.btn_drawnumbers[2].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[3].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[4].isFlat(), True)
        self.assertEqual(dialog.btnnumerarybonus[0].isFlat(), False)
        self.assertEqual(dialog.btnnumerarybonus[1].isFlat(), False)
        self.assertEqual(dialog.btnnumerarybonus[2].isFlat(), True)

    def test_highernumbers(self):
        """test with higher draw numbers as the highest number in the draw
        in the ball numbers and in the bonus numbers

        :return: none
        """
        dialog = DlgShowDrawing([2, 4, 6], 5, [1, 3, 5], 3)
        self.assertTrue(dialog)
        self.assertEqual(dialog.btn_drawnumbers[0].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[1].isFlat(), False)
        self.assertEqual(dialog.btn_drawnumbers[2].isFlat(), True)
        self.assertEqual(dialog.btn_drawnumbers[3].isFlat(), False)
        self.assertEqual(dialog.btn_drawnumbers[4].isFlat(), True)
        self.assertEqual(len(dialog.btn_drawnumbers), 5)
        self.assertEqual(dialog.btnnumerarybonus[0].isFlat(), False)
        self.assertEqual(dialog.btnnumerarybonus[1].isFlat(), True)
        self.assertEqual(dialog.btnnumerarybonus[2].isFlat(), False)
        self.assertEqual(len(dialog.btnnumerarybonus), 3)


if __name__ == '__main__':
    unittest.main()
