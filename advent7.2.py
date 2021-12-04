import copy

def par_def(comm_str, lst, i):
    param = []
    for j in range(3):
        if int(comm_str[-j-3]): #1 = True = immediate mode
            param.append(i+1+j)
        else:                   #0 = False = position mode
            param.append(lst[i+1+j])
    return param

with open('input7.1.txt') as f:
    lst = list(map(int, f.read().split(',')))

start_lst_lst = []
for i in range(5):
    start_lst_lst.append(lst.copy())
#print(lst_lst)

def run_once(lst1, inpt1, inpt2, i, input_count):
    opcode = 0
    while i < len(lst1):
        command = str(lst1[i])
        while len(command) < 5:
            command = "0" + command
        opcode = int(command[-2] + command[-1])
        if opcode!= 99 and opcode!= 3 and opcode!= 4:
            parameter = par_def(command, lst1, i)
        if opcode == 1:             #addition
            lst1[parameter[2]] = lst1[parameter[0]] + lst1[parameter[1]]
            i += 4
        elif opcode == 2:           #multiplying
            lst1[parameter[2]] = lst1[parameter[0]] * lst1[parameter[1]]
            i += 4
        elif opcode == 3:           #save input
            if input_count == False:
                lst1[lst1[i+1]] = inpt1
                input_count = True
            else:
                lst1[lst1[i+1]] = inpt2
            i += 2
        elif opcode == 4:           #get output
            if command[-3] == "1":
                parameter[0] = i + 1
            else:
                parameter[0] = lst1[i + 1]
            i += 2
            return lst1[parameter[0]], False, i, input_count
        elif opcode == 5:
            if lst1[parameter[0]] != 0:
                i = lst1[parameter[1]]
            else:
                i += 3
        elif opcode == 6:
            if lst1[parameter[0]] == 0:
                i = lst1[parameter[1]]
            else:
                i += 3
        elif opcode == 7:
            if lst1[parameter[0]] < lst1[parameter[1]]:
                lst1[parameter[2]] = 1
            else:
                lst1[parameter[2]] = 0
            i += 4
        elif opcode == 8:
            if lst1[parameter[0]] == lst1[parameter[1]]:
                lst1[parameter[2]] = 1
            else:
                lst1[parameter[2]] = 0
            i += 4
        elif opcode == 99:          #halt
            return 0, True, i, input_count
        else:                       #error
            print('Error! Unknown opcode', opcode)
            return 0, True, i, input_count

with open('input77.txt') as f:
    phase_all = list(f.read().split(','))
#phase_all2 = []
#for i in range(56789,98766):
#    j = str(i)
#    if j.count("5") == j.count("6") == j.count("7") == j.count("8") == j.count("9") == 1:
#        phase_all2.append(j)
#print(phase_all2)

max_output = 0
for phase in phase_all:
    lst_lst = copy.deepcopy(start_lst_lst)
    inpt = 0
    pos = [0, 0, 0, 0, 0]
    input_count = [False, False, False, False, False]
    halt_or_not = False
    last_outputE = 0
    while halt_or_not == False:
        for i, elem_ph in enumerate(phase):
#            print(i, inpt)
            result, halt_or_not, pos[i], input_count[i] = run_once(lst_lst[i], int(elem_ph), inpt, pos[i], input_count[i])
            if halt_or_not == False:
                inpt = result
                if i == 4:
                    last_outputE = result
            else:
                 break
    if last_outputE > max_output:
        max_output = last_outputE
        max_output_phase = phase
print("max_output =", max_output)
print("max_output_phase =", max_output_phase)

