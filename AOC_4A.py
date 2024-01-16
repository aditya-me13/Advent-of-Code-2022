count = 0
while True:
    ls1, ls2 = input().split(',')
    if ls1 == "exit":
        break
    else:
        f1, f2 = ls1.split('-')
        s1, s2 = ls2.split('-')
        f1, s1, f2, s2 = int(f1), int(s1), int(f2), int(s2)
        if f1<=s1<=s2<=f2 :
            count += 1
        elif s1<=f1<=f2<=s2:
            count += 1
        else:
            count += 0
print(count)