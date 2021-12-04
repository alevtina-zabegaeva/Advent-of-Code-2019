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

inpt = 1
opcode = 0
for i in range(0,len(lst),2):
    if opcode == 1 or opcode == 2:
        opcode = 0
        continue
    command = str(lst[i])
    while len(command) < 5:
        command = "0" + command
    opcode = int(command[-2] + command[-1])
    parameter = par_def(command, lst, i)
    if opcode == 1:             #addition
        lst[parameter[2]] = lst[parameter[0]] + lst[parameter[1]]
    elif opcode == 2:           #multiplying
        lst[parameter[2]] = lst[parameter[0]] * lst[parameter[1]]
    elif opcode == 3:           #save input
        lst[lst[i+1]] = inpt
    elif opcode == 4:           #get output
        outpt = lst[parameter[0]]
        print("Output =", outpt)
    elif opcode == 99:          #halt
        print('Halt')
        break
    else:                       #error
        print('Error! Unknown opcode', opcode)
        break


