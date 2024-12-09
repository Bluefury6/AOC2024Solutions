l1 = []
l2 = []
d = 0

with open("inputs/input1.txt", "r") as input:
    pairs = input.read().split("\n")
    for val in pairs:
        l1.append(int(val.split('   ')[0]))
        l2.append(int(val.split('   ')[1]))

    l1.sort()
    l2.sort()

    for i, val in enumerate(l1):
        d += abs(l2[i] - l1[i])

    print(d)