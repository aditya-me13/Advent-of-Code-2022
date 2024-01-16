count = 0
while True:
    ls1, ls2 = input().split(',')
    if ls1 == 'exit':
        break
    else:
        list1 = []
        list2 = []
        f1, f2 = ls1.split('-')
        s1, s2 = ls2.split('-')
        f1, f2, s1, s2 = int(f1), int(f2), int(s1), int(s2)


        i = 0
        x = (f2 - f1 + 1)
        y = (f2 - f1)
        while i < x:
            list1.append(f1)
            f1 += 1
            i += 1


        i = 0
        x = (s2 - s1 + 1)
        while i < x:
            list2.append(s1)
            s1 += 1
            i += 1

        stop = False
        for ls in list2:
            i = 0
            if stop == True:
                break
            while i <= y:
                if ls == list1[i]:
                    count+=1
                    stop = True
                i += 1
print(count)





