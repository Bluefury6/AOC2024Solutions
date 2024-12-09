count = 0

def isAntinode(point, nodes):
    for i, node in enumerate(nodes):
        dx, dy = node[0] - point[0], node[1] - point[1]
        for j, other in enumerate(nodes):
            if j == i:
                continue
            dx2, dy2 = other[0] - point[0], other[1] - point[1]
            if (dy == 0 and dx == 0) or (dy2 == 0 and dx2 == 0):
                return True
            if 0 in [dx, dy, dx2, dy2]:
                if dx == dx2 or dy == dy2:
                    return True
                else:
                    continue
            if dy/dx == dy2/dx2:
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