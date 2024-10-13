# -*- coding: utf-8 -*-

# pyLottoSimu

# Copyright (C) <2012-2024> Markus Hackspacher

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

import operator
from collections import Counter

import pylottosimu.pylotto


class statistic():
    @classmethod
    def uniform_distribution(cls):
        lotto_distribution = pylottosimu.pylotto.DrawLotto()
        lotto_times = []
        for _ in range(10000):
            lotto_distribution.draw()
            lotto_times += lotto_distribution.random_number
        c = Counter(lotto_times)
        print("max: {0}, min: {1}".format(
            max(c.items(), key=operator.itemgetter(1)),
            min(c.items(), key=operator.itemgetter(1))))
        print("{}".format(len(lotto_times) / 49))
        return c
