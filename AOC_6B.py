ls = input()
i = 0
found = False
while i < len(ls):
    if found == True:
        break
    j = 0
    found2 = False
    while j < 14:
        k = 0
        if found2 == True:
            break
        while k < j:
            if ls[i+j] == ls[i+k]:
                found2 = True
            k += 1
        j += 1
    if found2 == False:
        print(i + 14)
        found = True
    i += 1

