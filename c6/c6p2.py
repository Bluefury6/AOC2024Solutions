count = 0
def printGrid(grid):
    for line in grid:
        print("".join([c[0] for c in line]))
    print("\n")

with open("inputs/input6.txt") as t:
    lines = t.read().split("\n")
    baseGrid = [list(line) for line in lines]
    grid = list(baseGrid)

    start = [0, 0]
    for i, line in enumerate(lines):
        if "^" in line:
            start = [line.index("^"), i]

    pos = [start[0], start[1]]
    dir = [0, 1]
    
    def runSim(grid):
        while not (pos[0] + dir[0] < 0 or pos[0] + dir[0] >= len(grid[0]) or pos[1] - dir[1] < 0 or pos[1] - dir[1] >= len(grid)):
            isLooping = False
            i = 0
            while grid[pos[1] - dir[1]][pos[0] + dir[0]][:1] == "#":
                
                tempX = dir[0]
                dir[0] = dir[1]
                dir[1] = -tempX
                i += 1
                if str(dir) == grid[pos[1]][pos[0]][2:]:
                    global count
                    count += 1
                    isLooping = True
                # if i > 1:
                #     grid[pos[1]][pos[0]] = "|"
                #     printGrid(grid)
                #     # break
                    
            if isLooping:
                break

            grid[pos[1]][pos[0]] = "X " + str(dir)
            pos[0] += dir[0]
            pos[1] -= dir[1]
        
        grid[pos[1]][pos[0]] = "X " + str(dir)
        return grid

    possibleBlockPositions = []
    for y, posi in enumerate(runSim(baseGrid)):
        for x, val in enumerate(posi):
            if val[0] == "X":
                possibleBlockPositions.append((x, y))

    for i, obstaclePos in enumerate(possibleBlockPositions):
        if i / len(possibleBlockPositions) // 0.01 != (i-1) / len(possibleBlockPositions) // 0.01:
            print(f"{(100*i)//len(possibleBlockPositions)}%")
        if obstaclePos[0] == start[0] and obstaclePos[1] == start[1]:
            continue
        
        grid = [list(line) for line in lines]
        
        grid[obstaclePos[1]][obstaclePos[0]] = "#"
        
        pos = [start[0], start[1]]
        dir = [0, 1]
        runSim(grid)


    print(count, len(possibleBlockPositions))