score = 0
while True:
    you, me = input().split(" ")

    if you == "exit":
        break

    if me == "X":
        score += 1
    elif me == "Y":
        score += 2
    elif me == "Z":
        score += 3

    if you == "A":
        if me == "Y":
            score += 6
        elif me == "Z":
            score += 0
        elif me == "X":
            score += 3
    elif you == "B":
        if me == "X":
            score += 0
        elif me == "Z":
            score += 6
        elif me == "Y":
            score += 3
    elif you == "C":
        if me == "X":
            score += 6
        elif me == "Y":
            score += 0
        elif me == "Z":
            score += 3
print(score)
