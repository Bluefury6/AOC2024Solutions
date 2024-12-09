l1 = []
l2 = []
nums = []
s = 0

with open("inputs/input1.txt", "r") as input:
    pairs = input.read().split("\n")
    for val in pairs:
        l1.append(int(val.split('   ')[0]))
        if int(val.split('   ')[0]) not in nums:
            nums.append(int(val.split('   ')[0]))

        l2.append(int(val.split('   ')[1]))

    for num in nums:
        s += num*l2.count(num)

    print(s)

    input.close()