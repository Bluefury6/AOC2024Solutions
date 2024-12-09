with open("inputs/input9.txt", "r") as text:
    diskMap = list(text.read())
    blocks = [[i for _ in range(int(v))] for i, v in enumerate(diskMap[::2])]
    spaces = [list("."*int(v)) for v in diskMap[1::2]]
    full = []
    for i, val in enumerate(blocks):
        full.append(val)
        if i >= len(spaces):
            continue
        full.append(spaces[i])
    full = sum(full, [])

    for i, val in enumerate(full[::-1]):
        if "." not in full:
            break
        if full.index(".") >= len(full) - i:
            continue
        full[full.index(".")] = val
        full[len(full) - 1 - i] = ""

    full = full[:full.index("")]

    count = 0
    for i, val in enumerate(full):
        count += i*val
    print(count)