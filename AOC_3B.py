ls = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sm = 0
while True:
    x = input()
    if x == "exit":
        break
    else :
        count = 0
        while count < 3:
            if count == 0:
                x1 = x
                x = input()
            elif count == 1:
                x2 = x
                x = input()
            elif count == 2:
                x3 = x
            count += 1
        i = 0
        while i < len(ls):
            if ((ls[i] in x1)==True) and ((ls[i] in x2)==True) and ((ls[i] in x3)==True):
                sm = sm + i + 1
                break
            i += 1
print(sm)
