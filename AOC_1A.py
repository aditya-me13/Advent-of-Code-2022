mx = 0
while True:
    su = 0
    num = input()
    if num == "exit":
        break
    while num != '':
        su = su + int(num)
        num = input()
    if su > mx :
        mx = su
print(mx)