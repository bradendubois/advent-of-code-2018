from sys import stdin
from time import sleep
import re


def second(points):
    return {(x + d_x, y + d_y, d_x, d_y) for x, y, d_x, d_y in points}


def ranges(points):

    x = [point[0] for point in points]
    y = [point[1] for point in points]

    return min(x), max(x), min(y), max(y)


def display(points):

    min_x, max_x, min_y, max_y = ranges(points)
    xy_points = {(x, y) for x, y, d_x, d_y in points}

    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            if (x, y) in xy_points:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


velocities = stdin.read().split("\n")

points = set()

for instruction in velocities:
    
    x, y, d_x, d_y = [int(d) for d in re.findall(r'-?\d+', instruction)]
    points.add((x, y, d_x, d_y))


seconds = 0

while True:
    min_x, max_x, min_y, max_y = ranges(points)
    if abs(max_y - min_y) < 50 and abs(max_x - min_x) < 100:
        print("At", seconds, "seconds.")
        display(points)
        sleep(1)

    points = second(points)
    seconds += 1
