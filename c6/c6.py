count = 0

with open("inputs/input6.txt") as t:
    lines = t.read().split("\n")
    grid = [list(line) for line in lines]
    
    start = [0, 0]
    for i, line in enumerate(lines):
        if "^" in line:
            start = [line.index("^"), i]
    
    pos = [start[0], start[1]]
    dir = [0, 1]
    while not (pos[0] + dir[0] < 0 or pos[0] + dir[0] >= len(grid[0]) or pos[1] - dir[1] < 0 or pos[1] - dir[1] >= len(grid)):
        if grid[pos[1] - dir[1]][pos[0] + dir[0]] == "#":
            tempX = dir[0]
            dir[0] = dir[1]
            dir[1] = -tempX
        
        grid[pos[1]][pos[0]] = "X"
        pos[0] += dir[0]
        pos[1] -= dir[1]
        

    for line in grid:
        count += line.count("X")
    
    for line in grid:
        print("".join(line))
    print("\n", pos)

    print(count + 1)