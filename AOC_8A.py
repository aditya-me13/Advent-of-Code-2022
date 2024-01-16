no_of_lines = 0
mat = []
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
req_trees = []
i = 0 # ith column
while i < no_of_lines:
    j = 0 # jth column
    while j < no_of_rows :
        num_to_check = mat[i][j]

        flag = False
        for n in range(j):
            if mat[i][n] >= num_to_check:
                flag = True
                break
        if ((f'{i}/{j}' in req_trees) == False) and (flag == False):
            req_trees.append(f'{i}/{j}')

        flag = False        
        for n in range(i):
            if mat[n][j] >= num_to_check:
                flag = True
                break
        if ((f'{i}/{j}' in req_trees) == False) and (flag == False):
            req_trees.append(f'{i}/{j}')

        flag = False    
        for n in range(no_of_rows-1-j):
            if mat[i][no_of_rows-1-n] >= num_to_check:
                flag = True
                break
        if ((f'{i}/{j}' in req_trees) == False) and (flag == False):
            req_trees.append(f'{i}/{j}')

        flag = False
        for n in range(no_of_lines-1-i):
            if mat[no_of_lines-1-n][j] >= num_to_check:
                flag = True
                break
        if ((f'{i}/{j}' in req_trees) == False) and (flag == False):
            req_trees.append(f'{i}/{j}')   
        j += 1
    i += 1                 
print(len(req_trees))