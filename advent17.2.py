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

with open('input17.1.txt') as f:
    lst = list(map(int, f.read().split(',')))

lst[0] = 2
inpt = 2
opcode = 0
i = 0
rel_base = 0
map1 = []
array1 = []

A = 'L,8,R,10,L,8,R,8'
B = 'L,12,R,8,R,8'
C = 'L,8,R,6,R,6,R,10,L,8'
routine = 'A,B,A,C,C,A,B,C,B,B'

inp_lst = []
for elem in routine:
    inp_lst.append(ord(elem))
inp_lst.append(10)
for elem in A:
    inp_lst.append(ord(elem))
inp_lst.append(10)
for elem in B:
    inp_lst.append(ord(elem))
inp_lst.append(10)
for elem in C:
    inp_lst.append(ord(elem))
inp_lst.append(10)
inp_lst = tuple(inp_lst)

inp_ind = 0

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
        if inp_ind < len(inp_lst):
            lst[parameter] = inp_lst[inp_ind]
            inp_ind += 1
        elif inp_ind == len(inp_lst):
            lst[parameter] = ord('n')
            inp_ind += 1
        else:
            lst[parameter] = 10
            inp_ind = 0
        i += 2
    elif opcode == 4:           #get output
        outpt = lst[parameter]
        if inp_ind >= len(inp_lst):
            print(chr(outpt), end = '')
        if outpt == 10:
            map1.append(array1)
            array1 = []
        else:
            array1.append(chr(outpt))
        if outpt > 127:
            print('Output =', outpt)
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

map1 = map1[:-1]

for stroka in map1:
    for elem in stroka:
        print(elem, end = '')
    print()

