import numpy as np
from np_baseball import np_baseball

# print(np_baseball)

"""
Az `np_baseball` 2D-s tömb 3 oszloppal rendelkezik: magasság (inch), tömeg, kor.

Valami viszont azt súgja, hogy kiugróan magas értékek is vannak a tömbben...

# ez legyen egy numpy tömb, ami az np_baseball 1. oszlopát tartalmazza
np_height =

+ nyomtassuk ki az np_height átlagát
+ nyomtassuk ki az np_height medián értékét
"""

np_height = np.array(np_baseball[:, 0])
print(np.mean(np_height))
print(np.median(np_height))
