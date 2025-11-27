"""
Legyen adott a köv. lista:

    baseball = [180, 215, 210, 210, 188, 176, 209, 200]

ami baseball játékosok magasságát tartalmazza (cm-ben).

    # importáljuk a numpy modult
    import ...

    # készítsünk egy numpy tömböt a fenti listából
    np_baseball = ...

    # írassuk ki np_baseball típusát
    print(...)
"""
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

np_bb = np.array(baseball)
print(type(np_bb))
