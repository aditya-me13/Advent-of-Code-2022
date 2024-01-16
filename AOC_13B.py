inp, count, lss = [], 0, []

# Input:
while True:
    x = input()
    if x == 'exit':
        break
    if x == '':
        continue
    inp.append(x)
inp.append('[[2]]')
inp.append('[[6]]')


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
lss.insert(0, eval((inp[0])))
for i in range(0, len(inp)):
    lx = eval(inp[i])
    k = len(lss)
    flag = False
    for m in range(k):
        if check(lx, lss[m]):
            lss.insert(m, lx)
            flag = True
            break
        else:
            flag = False
    if flag == False:
        lss.insert(-1, lx)

lss = lss[:-1]
n1 = lss.index([[2]]) + 1
n2 = lss.index([[6]]) + 1
print(n1*n2)
