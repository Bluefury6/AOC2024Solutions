count = 0

with open("inputs/input4.txt", "r") as input:
    rawText = input.read()
    lines = rawText.split("\n")
    arr =  [list(line) for line in lines]
    
    for y, line in enumerate(arr):
        for x, letter in enumerate(line):
            if letter == 'X':
                if not x < 3:
                    if line[x-1]+line[x-2]+line[x-3] == "MAS":
                        count += 1
                if not x > len(line) - 4:
                    if line[x+1]+line[x+2]+line[x+3] == "MAS":
                        count += 1

                if not y < 3:
                    if arr[y-1][x]+arr[y-2][x]+arr[y-3][x] == "MAS":
                        count += 1
                if not y > len(arr) - 4:
                    if arr[y+1][x]+arr[y+2][x]+arr[y+3][x] == "MAS":
                        count += 1

                if not x < 3 and not y < 3:
                    if arr[y-1][x-1]+arr[y-2][x-2]+arr[y-3][x-3] == "MAS":
                        count += 1
                if not x < 3 and not y > len(arr) - 4:
                    if arr[y+1][x-1]+arr[y+2][x-2]+arr[y+3][x-3] == "MAS":
                        count += 1
                if not x > len(line) - 4 and not y < 3:
                    if arr[y-1][x+1]+arr[y-2][x+2]+arr[y-3][x+3] == "MAS":
                        count += 1
                if not x > len(line) - 4 and not y > len(arr) - 4:
                    if arr[y+1][x+1]+arr[y+2][x+2]+arr[y+3][x+3] == "MAS":
                        count += 1

    print(count)