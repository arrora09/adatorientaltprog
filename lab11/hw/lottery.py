import time

from typing import List


def lottery() -> List[int]:
    for i1 in range(46):
        for i2 in range(i1, 46):
            for i3 in range(i2, 46):
                for i4 in range(i3, 46):
                    for i5 in range(i4, 46):
                        for i6 in range(i5, 46):
                            if (
                                i1 + i2 + i3 + i4 + i5 + i6 == 90
                                and i1 * i2 * i3 * i4 * i5 * i6 == 996300
                            ):
                                return [i1, i2, i3, i4, i5, i6]


if __name__ == "__main__":
    start = time.time()
    print(lottery())
    print(time.time() - start)
