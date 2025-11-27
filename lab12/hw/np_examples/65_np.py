import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# sorba fuz ossze, egymas moge
print(np.hstack([a, b]))

# oszlopba fuz ossze, egymas ala
print(np.vstack([a, b]))

# elemenkent egymas ala
print(np.column_stack((a, b)))
