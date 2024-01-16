ls = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sm = 0
while True:
    x = input()
    if x == "exit":
        break
    else:
        f, s = x[:int((len(x)/2))], x[int((len(x)/2)):]
        i = 0
        while i < len(f):
            j = 0
            found = False
            while j < len(s):
                if f[i] == s[j]:
                    sm = sm + int(ls.find(f[i])) + 1
                    found = True
                    break
                j += 1
            if found == True:
                break
            i += 1
print(sm)


