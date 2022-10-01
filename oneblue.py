# Oneblue
# ===
# GNU General Public License v3.0, This file is part of Oneblue.
#             Copyright (C) 2022 凪坤 (GitHub ID: sandyzikun)
# -*-
# Oneblue is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# -*-
# Oneblue is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# -*-
# You should have received a copy of the GNU General Public License
# along with Oneblue. If not, see <https://www.gnu.org/licenses/>.
# -*-
__author__ = "sandyzikun"
__version__ = "0.0.3"
import numpy as np
from matplotlib import pyplot as plt
def colorparse(color):
    if isinstance(color, str):
        assert color[0] == "#" and len(color) in [ 4, 5, 7, 9 ]
        color = color.lower()
        for k in range(1, len(color)):
            assert color[k] in "0123456789abcdef"
        if len(color) < 6:
            color = np.array([ (int(color[     k + 1 :     k + 2 ], 16) /  15) for k in range(3) ])
        else:
            color = np.array([ (int(color[ 2 * k + 1 : 2 * k + 3 ], 16) / 255) for k in range(3) ])
    else:
        color = np.array(color).flatten().astype(np.float64)[ : 3 ]
        assert 0 <= color.min() < color.max() <= 1
    return color.min(), color.max() - color.min()
class Single_Color_Sequence(object):
    def __init__(self, psi=( 0, (6/9+7/11)/2, 1 ), nameprefix="oneblue"):
        self.psi = np.array(psi).reshape(3).astype(np.float64)
        # Normalization
        self.psi -= self.psi.min()
        self.psi /= self.psi.max()
        self.cmap = self.generate("%s_cmap" % nameprefix, [ "#011", "#025", "#069", "#18c",
                                                            "#3ae", "#6cf", "#acf", "#eff" ])
        self.dmap = self.divermap("%s_dmap" % nameprefix, ([ .3, 1. ], [ 1., .5 ]))
    def generate(self, name, colorarr, scalearr=None):
        colors = []
        for eachcolor in colorarr:
            cmin, csat = colorparse(eachcolor)
            colors.append(csat * self.psi + cmin)
        if not scalearr:
            nodes = np.linspace(0, 1, len(colors), endpoint=True)
        else:
            nodes = np.array(scalearr).flatten().astype(np.float64)
        return plt.matplotlib.colors.LinearSegmentedColormap.from_list(name, list(zip(nodes, colors)))
    def divermap(self, name, lvals, another=( 1, 0, 0 )):
        ano = np.array(another).reshape(3).astype(np.float64)
        nodes = np.concatenate([
            np.linspace(0., .5, len(lvals[0]) + 1, endpoint=True)[ : -1 ],
            np.linspace(.5, 1., len(lvals[1]) + 1, endpoint=True),
            ])
        colors = tuple( lval * self.psi for lval in lvals[0] ) + (np.ones(3),) + \
                 tuple( lval *      ano for lval in lvals[1] )
        return plt.matplotlib.colors.LinearSegmentedColormap.from_list(name, list(zip(nodes, colors)))
oneb1ue = Single_Color_Sequence()