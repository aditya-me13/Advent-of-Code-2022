row1 = ['V', 'N','F', 'S', 'M', 'P', 'H', 'J']
row2 = ['Q', 'D', 'J', 'M', 'L', 'R', 'S']
row3 = ['B', 'W', 'S', 'C', 'H', 'D', 'Q', 'N']
row4 = ['L', 'C', 'S', 'R']
row5 = ['B', 'F', 'P', 'T', 'V', 'M']
row6 = ['C', 'N', 'Q', 'R', 'T']
row7 = ['R', 'V', 'G']
row8 = ['R', 'L', 'D', 'P', 'S', 'Z', 'C']
row9 = ['F', 'B', 'P', 'G', 'V', 'J', 'S', 'D']
matrix = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
while True:
    inp = input()
    if inp == "exit":
        break
    else:
        a,b,c,d,e,f = inp.split()
        num_box, drop, pick = int(b), int(d), int(f)
        i = 0
        while i < num_box:
            value = matrix[drop-1][0]
            matrix[drop-1].pop(0)
            matrix[pick-1].insert(0, value)
            i += 1
i = 0
while i < 9:
    print(matrix[i][0], end = "")
    i += 1


