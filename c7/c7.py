count = 0

def generatePossibilities(n):
    l = [["+"], ["*"]]
    for i in range(n - 1):
        l2 = []
        for li in l:
            for val in ["+", "*"]:
                l2.append(li + [val])
        l = l2

    return l

with open("inputs/input7.txt", "r") as input:
    lines = [[int(v) for v in "".join(line.split(":")).split(" ")] for line in input.read().split("\n")]
    for j, line in enumerate(lines):
        print(j/len(lines), len(generatePossibilities(len(line) - 2)))
        for poss in generatePossibilities(len(line) - 2):
            outputVal = line[0]
            testVal = line[1]
            for i, val in enumerate(line[2:]):
                exec(f"testVal {poss[i - 1]}= {val}")
            
            if testVal == outputVal:
                count += outputVal
                break

print(count)