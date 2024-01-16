inp, ip = input(), []
while True:
    if inp == "exit":
        break
    ip.append(inp)
    inp = input()
H = (0, 0)
T = (0, 0)
move_x = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
move_y = {'R': 0, 'L': 0, 'U': 1, 'D': -1}
st = set({})
for inp in ip:
    move, val = inp.split()
    for n in range(int(val)):
        H = (H[0] + move_x[move], H[1] + move_y[move])
        if H[0] == T[0] and (H[1] - T[1] == 2):
            T = (T[0], T[1] + 1)
        elif H[0] == T[0] and (H[1] - T[1] == -2):
            T = (T[0], T[1] - 1)
        elif H[1] == T[1] and (H[0] - T[0] == 2):
            T = (T[0] + 1, T[1])
        elif H[1] == T[1] and (H[0] - T[0] == -2):
            T = (T[0] - 1, T[1])
        elif H[0] != T[0]:
            if H[0] > T[0] and H[1] > T[1] and (H[1] - T[1] == 2):
                T = (T[0] + 1, T[1] + 1)
            elif H[0] > T[0] and H[1] > T[1] and (H[0] - T[0] == 2):
                T = (T[0] + 1, T[1] + 1)
            elif H[0] > T[0] and H[1] < T[1] and (H[0] - T[0] == 2):
                T = (T[0] + 1, T[1] - 1)
            elif H[0] > T[0] and H[1] < T[1] and (H[1] - T[1] == -2):
                T = (T[0] + 1, T[1] - 1)
            elif H[0] < T[0] and H[1] > T[1] and (H[0] - T[0] == -2):
                T = (T[0] - 1, T[1] + 1)
            elif H[0] < T[0] and H[1] > T[1] and (H[1] - T[1] == 2):
                T = (T[0] - 1, T[1] + 1)
            elif H[0] < T[0] and H[1] < T[1] and (H[0] - T[0] == -2):
                T = (T[0] - 1, T[1] - 1)
            elif H[0] < T[0] and H[1] < T[1] and (H[1] - T[1] == -2):
                T = (T[0] - 1, T[1] - 1)
        st.add(T)
print(len(st))
