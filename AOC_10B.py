i, signal_value, j, index = 0, 1, 1, 0
whatWeNeed = [list(40*"."), list(40*"."), list(40*"."), list(40*"."), list(40*"."), list(40*".")]
while True:
    inp = input()
    if inp == "exit":
        break
    else:
        if i > 40:
            i = i - 40
            index += 1
        ls = [j, j+1, j+2]
        if inp == 'noop':
            i += 1
            if i in ls:
                whatWeNeed[index][i-1] = '#'
            if i > 40:
                i = i - 40
                index += 1
        else:
            i += 1
            if i in ls:
                whatWeNeed[index][i-1] = '#'
            if i > 40:
                i = i - 40
                index += 1
            i += 1
            if i in ls:
                whatWeNeed[index][i-1] = '#'
            j += int(inp.split()[1])
for obj in whatWeNeed:
    print(''.join(obj))