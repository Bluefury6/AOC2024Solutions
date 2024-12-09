import re
count = 0

with open("inputs/input3.txt", "r") as input:
    text = input.read()
    string = re.compile("mul\(\d*,\d*\)")
    vals = string.findall(text)
    locs = [m.end() for m in string.finditer(text)]

    for i, val in enumerate(vals):
        if "don't" in text[0:locs[i]]:
            donts = [m.end() for m in re.compile("don\'t\(\)").finditer(text[0:locs[i]])]
            if "do()" not in text[donts[len(donts)-1]:locs[i]]:
                continue
        val = val.split(",")
        count += int(val[0][4:]) * int(val[1][:-1])

    print(count)