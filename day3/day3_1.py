res = 0
import re
import numpy as np

with open("input_1.txt") as f:
    data = f.read()
    lines = data.splitlines()
    s = 0
    for y, line in enumerate(data[2:-2], start=2):
        x0 = -1

        for x, c in enumerate(line[2:-1], start=2):
            if c.isdigit():
                if x0 == -1:
                    x0 = x

            elif x0 != -1:
                window = data[y - 1:y + 2, x0 - 1:x + 1]

                if np.any((window != ".") & (~np.char.isdigit(window))):
                    s += int("".join(line[x0:x]))

                x0 = -1

    print(s)
