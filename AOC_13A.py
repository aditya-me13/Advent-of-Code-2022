inp = []
count = 0

# Input:
while True:
    x = input()
    if x == 'exit':
        break
    if x == '':
        continue
    inp.append(x)


# Function
def check(ls1, ls2):
    for n in range(min([len(ls2), len(ls1)])):
        if type(ls1[n]) == int and type(ls2[n]) == int:
            if ls1[n] < ls2[n]:
                return True
            elif ls1[n] > ls2[n]:
                return False
            elif ls1[n] == ls1[n]:
                continue
        elif type(ls1[n]) == int and type(ls2[n]) == list:
            ls = [ls1[n]]
            if check(ls, ls2[n]) in [True, False]:
                return check(ls, ls2[n])
            continue
        elif type(ls1[n]) == list and type(ls2[n]) == int:
            ls = [ls2[n]]
            if check(ls1[n], ls) in [True, False]:
                return check(ls1[n], ls)
            continue
        elif type(ls1[n]) == list and type(ls2[n]) == list:
            if check(ls1[n], ls2[n]) in [True, False]:
                return check(ls1[n], ls2[n])
            continue
    if len(ls1) == len(ls2):
        return None
    elif len(ls1) < len(ls2):
        return True
    elif len(ls1) > len(ls2):
        return False


# Processing:
for i in range(0, len(inp), 2):
    l1 = eval(inp[i])
    l2 = eval(inp[i + 1])
    if check(l1, l2):
        print((i // 2) + 1)
        count += (i // 2) + 1
print(count)
