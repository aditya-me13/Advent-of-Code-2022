inp = []
while True:
    x = input()
    if x == "exit":
        break
    inp.append(x)

path = []
directories = {}
for line in inp:
    if line.startswith('$'):
        if line.split()[1] == 'ls':
            continue
        elif line.split()[1] == 'cd':
            p, q, r = line.split()
            if r == '..':
                path = path[:-1]
            else:
                path.append(r)
                directories[','.join(path)] = 0
    elif line.startswith("dir"):
        continue
    else:
        mem, name = line.split()
        p = ','.join(path)
        directories[p] = directories[p] + int(mem)

for d in directories:
    ls = d.split(',')
    l = len(ls)
    for i in range(l - 1):
        ls.pop(-1)
        directories[','.join(ls)] += directories[d]

val, allowed_dir = directories['/'] - 40000000, []
for d in directories:
    if directories[d] >= val:
        allowed_dir.append(directories[d])
print(min(allowed_dir))
