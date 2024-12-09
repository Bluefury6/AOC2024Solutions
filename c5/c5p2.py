count = 0

def isOrdered(li, rules):
    for i, num in enumerate(li):
        for val in rules[num]:
            if val in li[:i]:
                return False

    return True

def updateSort(li, rules):
    while True:
        noProblems = True
        for i, val in enumerate(li):
            for rule in rules[val]:
                if rule in li[:i]:
                    li = li[:i-1] + [val, li[i-1]] + li[i+1:]
                    noProblems = False
                    break

        if noProblems:
            break
    return li

with open("inputs/input5.txt", "r") as rawTextInput:
    rawText = rawTextInput.read()
    rulePairs = [rule.split("|") for rule in rawText.split("\n\n")[0].split("\n")]
    updates = [text.split(",") for text in rawText.split("\n\n")[1].split("\n")]

    rules = {}
    for pair in rulePairs:
        if pair[0] not in rules.keys():
            rules[pair[0]] = []
        
        rules[pair[0]].append(pair[1])

    for update in updates:
        if not isOrdered(update, rules):
            update = updateSort(update, rules)
            count += int(update[int(len(update)/2)])

    print(count)