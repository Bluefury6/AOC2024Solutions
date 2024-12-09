count = 0

with open("inputs/input2.txt", "r") as input:
    reports = input.read().split("\n")
    for report in reports:
        levelsInit = report.split(" ")
        for j in range(len(levelsInit)):
            levels = levelsInit[0:j] + levelsInit[j+1:]
            diffs = []
            for i in range(len(levels)-1):
                diffs.append(int(levels[i+1]) - int(levels[i]))
            
            unsafe = False
            for diff in diffs:
                if abs(diff) > 3 or abs(diff) < 1 or diffs[0]*diff < 0:
                    unsafe = True
                    break

            if not unsafe:
                count += 1
                break
            

    print(count)