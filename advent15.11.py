from collections import defaultdict

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

with open('input15.1.txt') as f:
    lst = list(map(int, f.read().split(',')))

def print_map(map2):
    for m in map2:
        for n in m:
            print(n, end = '')
        print()

inpt = 0
opcode = 0
i = 0
rel_base = 0
k_start, l_start = 21, 21
k, l = k_start, l_start
map1 = [[' ']*41 for i in range(41)]
map1[l][k] = "D"
direct = (-1, 0)
ox_i, ox_j = 0, 0
first = True
tupik = False
while (l != l_start or k != k_start) or first:
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
        if map1[l + direct[1]][k - direct[0]] != "#": #no wall on the right
            next_coord = (direct[1], - direct[0])       #try go to the right
        elif map1[l + direct[0]][k + direct[1]] != "#": #no wall forward
            next_coord = (direct[0], direct[1])       #try go forward
        elif map1[l - direct[1]][k + direct[0]] != "#": #no wall on the left
            next_coord = ( - direct[1], direct[0])       #try go to the left
        else:
            next_coord = ( - direct[0], - direct[1])       #go back
            if ox_i != l or ox_j != k:
                tupik = True
        if next_coord == (-1, 0):
            inpt = 1
        elif next_coord == (0, 1):
            inpt = 4
        elif next_coord == (0, -1):
            inpt = 3
        else:
            inpt = 2
        lst[parameter] = inpt
        i += 2
    elif opcode == 4:           #get output
        outpt = lst[parameter]
        if outpt == 0:
            map1[l + next_coord[0]][k + next_coord[1]] = "#"
        else:
            first = False
            direct = next_coord
            if map1[l + next_coord[0]][k + next_coord[1]] == " ":
                tupik = False
            if tupik == True:
                map1[l][k] = "#"
            else:
                map1[l][k] = "."
            l += next_coord[0]
            k += next_coord[1]
            if outpt == 1:
                map1[l][k] = "D"
            else:
                map1[l][k] = "!"
                ox_i, ox_j = l, k
        i += 2
#        print_map(map1)
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
map1[ox_i][ox_j] = "!"
print_map(map1)
