goal = 19690720
with open('input2.txt') as f:
    start_lst = list(map(int, f.read().split(',')))

for noun in range(100):
    for verb in range(100):
        lst = list(start_lst)
        lst[1] = noun
        lst[2] = verb
        for i in range(0,len(lst),4):
            if lst[i] == 1:
                lst[lst[i+3]] = lst[lst[i + 1]] + lst[lst[i + 2]]
            elif lst[i] == 2:
                lst[lst[i+3]] = lst[lst[i + 1]] * lst[lst[i + 2]]
            elif lst[i] == 99:
                break
            else:
                print('Error!')
                break
        if lst[0] == goal:
            break
    if lst[0] == goal:
        break
print(noun, verb, 100*noun + verb)

