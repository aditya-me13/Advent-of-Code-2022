ls = input()
i = 0
found = False
while i < len(ls):
    if found == True:
        break
    if ls[i] != ls[i+1] and ls[i] != ls[i+2] and ls[i] != ls[i+3] and ls[i+1] != ls[i+2] and ls[i+1] != ls[i+3] and ls[i+2] != ls[i+3]:
        print(i + 4)
        found = True
    i += 1
