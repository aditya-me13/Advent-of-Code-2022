score = 0
while True:
    you, me = input().split(" ")
    if you == "exit":
        break
    if me == "X":
        score += 0
    elif me == "Y":
        score += 3
    elif me == "Z":
        score += 6

    if you == "A" :
        if me == "Y":
            score += 1
        elif me == "Z":
            score += 2
        elif me == "X":
            score += 3
    elif you == "B":
        if me == "X":
            score += 1
        elif me == "Z":
            score += 3
        elif me == "Y":
            score += 2
    elif you == "C":
        if me == "X":
            score += 2
        elif me == "Y":
            score += 3
        elif me == "Z":
            score += 1
print(score)

