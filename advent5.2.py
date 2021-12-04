def par_def(comm_str, lst, i):
    param = []
    for j in range(3):
        if int(command[-j-3]): #1 = True = immediate mode
            param.append(i+1+j)
        else:                   #0 = False = position mode
            param.append(lst[i+1+j])
    return param

with open('input5.txt') as f:
    lst = list(map(int, f.read().split(',')))

print("Enter input ID")
inpt = int(input())
opcode = 0
i = 0
while i < len(lst):
    command = str(lst[i])
    while len(command) < 5:
        command = "0" + command
    opcode = int(command[-2] + command[-1])
    if opcode!= 99 and opcode!= 3 and opcode!= 4:
        parameter = par_def(command, lst, i)
    if opcode == 1:             #addition
        lst[parameter[2]] = lst[parameter[0]] + lst[parameter[1]]
        i += 4
    elif opcode == 2:           #multiplying
        lst[parameter[2]] = lst[parameter[0]] * lst[parameter[1]]
        i += 4
    elif opcode == 3:           #save input
        lst[lst[i+1]] = inpt
        i += 2
    elif opcode == 4:           #get output
        if command[-3] == "1":
            parameter[0] = i + 1
        else:
            parameter[0] = lst[i + 1]
        outpt = lst[parameter[0]]
        print("Output =", outpt)
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
    elif opcode == 99:          #halt
        print('Halt')
        break
    else:                       #error
        print('Error! Unknown opcode', opcode)
        break


