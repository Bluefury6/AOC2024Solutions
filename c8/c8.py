import math
count = 0

def isAntinode(point, nodes):
    for i, node in enumerate(nodes):
        dx, dy = node[0] - point[0], node[1] - point[1]
        d = math.sqrt(dx*dx + dy*dy)
        if dx == 0 and dy == 0:
            continue
        for j, other in enumerate(nodes):
            if j == i:
                continue
            dx2, dy2 = other[0] - point[0], other[1] - point[1]
            d2 = math.sqrt(dx2*dx2 + dy2*dy2)
            if dx2 == 0 and dy2 == 0:
                continue
            if 0 in [dx, dy, dx2, dy2]:
                if d2/d == 2 and ((dx == dx2) or (dy == dy2)):
                    return True
                else:
                    continue
            if dy/dx == dy2/dx2 and d2/d == 2:
                return True
    return False

with open("inputs/input8.txt", "r") as text:
    grid = [list(line) for line in text.read().split("\n")]

    aPoints = {}

    for y, line in enumerate(grid):
        for x, val in enumerate(grid[y]):
            if val != ".":
                if val not in aPoints.keys():
                    aPoints[val] = [(x, y)]
                else:
                    aPoints[val].append((x, y))

    for y, line in enumerate(grid):
        for x, val in enumerate(grid[y]):
            for f in aPoints:
                if isAntinode((x, y), aPoints[f]):
                    grid[y][x] = "#"
                    count += 1
                    break

    print(count)