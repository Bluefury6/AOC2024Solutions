import re
count = 0

with open("inputs/input3.txt", "r") as input:
    text = input.read()
    string = re.compile("mul\(\d*,\d*\)")
    vals = string.findall(text)

    for val in vals:
        val = val.split(",")
        count += int(val[0][4:]) * int(val[1][:-1])

    print(count)