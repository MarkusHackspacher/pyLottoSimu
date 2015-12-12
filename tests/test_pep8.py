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

import unittest
import pep8


class TestCodeFormat(unittest.TestCase):
    """
    Test of the code format
    """

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=False)
        result = pep8style.check_files(['pylottosimu/pylotto.py',
                                        'setup.py',
                                        'tests/test_drawlotto.py',
                                        'tests/test_pep8.py',
                                        'tests/test_show_drawing.py',
                                        'tests/test_lottosystemdata.py',
                                        'tests/test_lottosettingdialog.py',
                                        'pylottosimu/lottosystem.py',
                                        'pylottosimu/dialog/show_drawing.py',
                                        'pylottosimu/dialog/'
                                        'lottosettingdialog.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
