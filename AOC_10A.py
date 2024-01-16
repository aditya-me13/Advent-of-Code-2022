i,signal_value,signal_strengths= 0,1,[]
while True:
    inp = input()
    if inp == "exit":
        break
    else:
        if inp == 'noop':
            i += 1
            if i in (20, 60, 100, 140, 180, 220):
                signal_strengths.append(i * signal_value)
        else:
            i += 1
            if i in (20, 60, 100, 140, 180, 220):
                signal_strengths.append(i * signal_value)
            i += 1
            if i in (20, 60, 100, 140, 180, 220):
                signal_strengths.append(i * signal_value)
            signal_value += int(inp.split()[1])
print(signal_strengths)
print(sum(signal_strengths))
