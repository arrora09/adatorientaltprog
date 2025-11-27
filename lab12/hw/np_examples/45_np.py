import numpy as np

a = [[1, 2, 3], [4, 5, 6]]

np_2d = np.array(a)
print(np_2d)

print(np_2d.shape)

print(np_2d[0])


# ugyan az
print(np_2d[1][2])
print(np_2d[1, 2])

# adott oszlop(ok)
print(np_2d[:, 1:3])


# adott sor(ok)
print(np_2d[1, :])
