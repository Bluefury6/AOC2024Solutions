count = 0

with open("inputs/input10.txt", "r") as text:
    grid = [list(line) for line in text.read().split("\n")]

    def findTrails(x, y):
        trailEnds = []
        if grid[y][x] == '9' and (x, y) not in trailEnds:
            return [(x, y)]
        for val in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            if val[0] < 0 or val[1] < 0 or val[0] > len(grid[0]) - 1 or val[1] > len(grid) - 1:
                continue
            if grid[val[1]][val[0]] == str(int(grid[y][x]) + 1):
                for end in findTrails(val[0], val[1]):
                    if end not in trailEnds:
                        trailEnds.append(end)

        return trailEnds

    for y, _ in enumerate(grid):
        for x, val in enumerate(grid[y]):
            if val == '0':
                count += len(findTrails(x, y))

    print(count)