# Making Matrix
no_of_lines = 0
mat = []
max = 0
while True:
    inp = input()
    if inp == "exit":
        break
    else:
        no_of_rows = len(inp)
        mat.append([])
        for j in range(len(inp)):
            mat[no_of_lines].append(int(inp[j]))
        no_of_lines += 1
print(mat)
# Checking Scenic Sscore of each Tree
i = 0
while i < no_of_lines:
    j = 0
    while j < no_of_rows :
        num_to_check = mat[i][j]

        c1 = 0
        for n in range(i+1,no_of_lines):
            if mat[n][j] >= num_to_check:
                c1 += 1
                break
            else :
                c1 += 1

        c2 = 0
        for n in range(j+1,no_of_rows):
            if mat[i][n] >= num_to_check:
                c2 += 1
                break
            else:
                c2 += 1

        c3 = 0
        n = i-1
        while n >= 0:
            if mat[n][j] >= num_to_check:
                c3 += 1
                break
            else:
                c3 += 1
            n -= 1

        c4 = 0
        n = j - 1
        while n >= 0:
            if mat[i][n] >= num_to_check:
                c4 += 1
                break
            else:
                c4 += 1
            n -= 1

        ss = 0
        ss = c1*c2*c3*c4
        if ss > max:
            max = ss
        j += 1
    i += 1
print(max)


