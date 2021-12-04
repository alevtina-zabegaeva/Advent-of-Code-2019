def par_def(comm_str, lst, i):
    param = []
    for j in range(3):
        if command[-j-3] == "1": #immediate mode
            param.append(i + 1 + j)
        elif command[-j-3] == "2": #relative mode
            param.append(lst[i + 1 + j] + rel_base)
        else:                   #0 = False = position mode
            param.append(lst[i + 1 + j])
        if param[j] >= len(lst):
            lst += [0]*(param[j] - len(lst) + 1)
    return param

def print_map(map3, w):
    for i in range(w):
        for j in range(w):
            if (i, j) in map3:
                print('#', end = '')
            else:
                print('.', end = '')
        print()

with open('input19.1.txt') as f:
    lst1 = list(map(int, f.read().split(',')))

wid = 1080
map1 = set()

k = 0
nachalo = 0
while k < wid:
    l = nachalo
    started = False
    while l < wid:
        inpt = l
        lst = lst1.copy()
        opcode = 0
        i = 0
        rel_base = 0
        while i < len(lst):
            command = str(lst[i])
            parameter = ""
            while len(command) < 5:
                command = "0" + command
            opcode = int(command[-2] + command[-1])
            if opcode!= 99 and opcode!= 3 and opcode!= 4 and opcode!= 9:
                parameter = par_def(command, lst, i)
            if opcode == 4 or opcode == 9 or opcode == 3:
                if command[-3] == "1":
                    parameter = i + 1
                elif command[-3] == "2":
                    parameter = int(lst[i + 1] + rel_base)
                else:
                    parameter = int(lst[i + 1])
                if parameter >= len(lst):
                    lst += [0]*(parameter - len(lst) + 1)
            if opcode == 1:             #addition
                lst[parameter[2]] = lst[parameter[0]] + lst[parameter[1]]
                i += 4
            elif opcode == 2:           #multiplying
                lst[parameter[2]] = lst[parameter[0]] * lst[parameter[1]]
                i += 4
            elif opcode == 3:           #save input
                lst[parameter] = inpt
#                print('Input =', inpt)
                inpt = k
                i += 2
            elif opcode == 4:           #get output
                outpt = lst[parameter]
#                print('Output =', outpt)
                if outpt == 1:
                    map1.add((k, l))
                    if started == False:
                        nachalo = l
                    started = True
                elif started == True:
                    l = wid
                i += 2
            elif opcode == 5:
                if lst[parameter[0]] != 0:
                    i = lst[parameter[1]]
                else:
                    i += 3
            elif opcode == 6:
                if lst[parameter[0]] == 0:
                    i = lst[parameter[1]]
                else:
                    i += 3
            elif opcode == 7:
                if lst[parameter[0]] < lst[parameter[1]]:
                    lst[parameter[2]] = 1
                else:
                    lst[parameter[2]] = 0
                i += 4
            elif opcode == 8:
                if lst[parameter[0]] == lst[parameter[1]]:
                    lst[parameter[2]] = 1
                else:
                    lst[parameter[2]] = 0
                i += 4
            elif opcode == 9:
                rel_base +=  lst[parameter]
                i += 2
            elif opcode == 99:          #halt
#                print('Halt')
                break
            else:                       #error
                print('Error! Unknown opcode', opcode)
                break
        l += 1
    k += 1

#print_map(map1, wid)

square = set()
for key in map1:
    flag = True
    for i in range(1, 100):
        if not ((key[0] + i, key[1]) in map1 and (key[0], key[1] + i) in map1):
            flag = False
            break
    if flag:
        print(key)
        square.add(key)
m = min(square)
print('Min =', m[1], '*10000 +', m[0])
