count = 0

with open("inputs/input4.txt", "r") as input:
    rawText = input.read()
    lines = rawText.split("\n")
    arr =  [list(line) for line in lines]
    
    for y, line in enumerate(arr):
        for x, letter in enumerate(line):
            if letter == 'A' and x >= 1 and x <= len(line) - 2 and y >= 1 and y <= len(arr) - 2:
                if arr[y+1][x+1] + arr[y-1][x-1] in ["MS", "SM"] and arr[y-1][x+1] + arr[y+1][x-1] in ["MS", "SM"]:
                    count += 1

    print(count)