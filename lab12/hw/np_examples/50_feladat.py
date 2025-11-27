"""
# legyen adott a köv. mátrix
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

* konvertáljuk egy 2D-s numpy tömbbé
* írassuk ki a méretét (dimenzióit)
* nyerjük ki a teljes második oszlopot
"""

import numpy as np

baseball = [[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]

np_bb = np.array(baseball)
print(np_bb.shape)
print(np_bb[:, 1])
