from itertools import product
from sys import stdin
import numpy as np

serial = int(stdin.read())

N = 300

grid = [[0] * N for _ in range(N)]

for x, y in product(list(range(1, N+1)), list(range(1, N+1))):

    rack_ID = x + 10
    power_level = rack_ID * y
    power_level += serial
    power_level *= rack_ID
    power_level = (power_level // 100) % 10
    power_level -= 5

    grid[x-1][y-1] = power_level


def power_search(power_grid, n):
    windows = sum(power_grid[x:x-n+1 or None, y:y-n+1 or None] for x in range(n) for y in range(n))
    loc = np.where(windows == int(windows.max()))
    return loc[0][0] + 1, loc[1][0] + 1, int(windows.max())


grid = np.array(grid)


# Part One
print(",".join(str(x) for x in power_search(grid, 3)[:-1]))


# Part Two
best_x, best_y, best_power, best_n = 0, 0, 0, 0

last = 0
negative_in_row = 0

for width in range(3, 300):
    
    x, y, power = power_search(grid, width)    

    if power > best_power:
        best_x, best_y, best_n = x, y, width
        best_power = power

    if power < last:
        negative_in_row += 1
    else:
        negative_in_row = 0
    
    if negative_in_row == 15:
        break

    last = power


print(",".join([str(x) for x in [best_x, best_y, best_n]]))
