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

with open('input11.1.txt') as f:
    lst = list(map(int, f.read().split(',')))

inpt = 0
opcode = 0
i = 0
rel_base = 0
m = 70
n = 61
x = 19
y = 21
direction = [0, 1]
waiting_paint = True
map1 = [[-1] * m for i in range(n)]

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
#    print("i =", i,"command = ", command,"parameter =", parameter, "opcode =", opcode, "rel_base =", rel_base)
    if opcode == 1:             #addition
        lst[parameter[2]] = lst[parameter[0]] + lst[parameter[1]]
        i += 4
    elif opcode == 2:           #multiplying
        lst[parameter[2]] = lst[parameter[0]] * lst[parameter[1]]
        i += 4
    elif opcode == 3:           #save input
        lst[parameter] = inpt
        i += 2
    elif opcode == 4:           #get output
        outpt = lst[parameter]
        if waiting_paint:
            map1[x][y] = outpt
            waiting_paint = False
        else:
            a = direction[0]
            if outpt == 0:
                direction[0] = -direction[1]
                direction[1] = a
            else:
                direction[0] = direction[1]
                direction[1] = -a
            x += direction[0]
            y += direction[1]
            waiting_paint = True
            if map1[x][y] == 1: 
                inpt = 1
            else:
                inpt = 0
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
        print('Halt')
        break
    else:                       #error
        print('Error! Unknown opcode', opcode)
        break
count = 0
for element in map1:
    for elem in element:
        if elem != -1:
            count += 1
print(count)
