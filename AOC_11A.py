no_of_monkeys, lis, info = int(input()), [], []
for n in range(no_of_monkeys):
    m_no = int(input().split()[1][0])
    items = input().strip().split(':')[1].split(', ')
    items = list(map(int, items))
    opr = input().strip().split(':')[1].strip()
    test = int(input().strip().split(':')[1].strip().split()[2])
    if_true = int(input().strip().split(':')[1].strip().split()[3])
    if_false = int(input().strip().split(':')[1].strip().split()[3])
    line = input()
    ls = [opr, test, if_true, if_false]
    lis.append(items)
    info.append(ls)
print(lis)
print(info)
round_inspection = []
for i in range(no_of_monkeys):
    round_inspection.append(0)
for i in range(20):
    for j in range(no_of_monkeys):
        for num in lis[j]:
            if info[j][0].split()[4] == 'old':
                if info[j][0].split()[3] == '+':
                    new = num + num
                elif info[j][0].split()[3] == '*':
                    new = num * num
            elif info[j][0].split()[3] == '+':
                new = num + int(info[j][0].split()[4])
            elif info[j][0].split()[3] == '*':
                new = num * int(info[j][0].split()[4])

            new = new // 3
            if new % int(info[j][1]) == 0:
                lis[info[j][2]].append(new)
            else:
                lis[info[j][3]].append(new)
        round_inspection[j] = round_inspection[j] + len(lis[j])
        lis[j] = []
print((sorted(round_inspection)[-2]) * (sorted(round_inspection)[-1]))
