mx1 = 0
mx2 = 0
mx3 = 0
while True:
    su = 0
    num = input()
    if num == "exit":
        break
    while num != '':
        su = su + int(num)
        num = input()
    if su > mx1 :
        mx1, mx2, mx3 = su, mx1, mx2
    elif su > mx2:
        mx2 , mx3 = su, mx2
    elif su > mx3:
        mx3 = su
print(mx1 + mx2 + mx3)