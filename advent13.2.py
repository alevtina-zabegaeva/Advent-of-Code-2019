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

with open('input13.1.txt') as f:
    lst = list(map(int, f.read().split(',')))

lst[0] = 2 #quarters

inpt = 0
opcode = 0
i = 0
rel_base = 0
outpt = [0, 0, 0]
out_index = 0
map1 = [[" "]*44 for i in range(24)]
paddle = 0
ball = 0
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
        for m in map1:
            for n in m:
                print(n, end = '')
            print()
        print()
        i += 2
    elif opcode == 4:           #get output
        outpt[out_index] = lst[parameter]
        if out_index == 2:
            if outpt[0] == -1 and outpt[1] == 0:
                score = outpt[2]
            else:
                map1[outpt[1]][outpt[0]] = outpt[2]
                if outpt[2] == 3:
                    paddle = outpt[0]
                if outpt[2] == 4:
                    ball = outpt[0]
                if paddle == ball:
                    inpt = 0
                elif paddle > ball:
                    inpt = -1
                else:
                    inpt = 1                
            out_index = 0
        else:
            out_index += 1
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

print(score)
