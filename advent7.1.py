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

def run_once(lst1, inpt1, inpt2):
    opcode = 0
    i = 0
    input_count = False
    while i < len(lst1):
        command = str(lst1[i])
        while len(command) < 5:
            command = "0" + command
        opcode = int(command[-2] + command[-1])
        if opcode!= 99:
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
            outpt1 = lst1[parameter[0]]
            i += 2
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
            break
        else:                       #error
            print('Error! Unknown opcode', opcode)
            break
    return outpt1

with open('input7.txt') as f:
    phase_all = list(f.read().split(','))
#phase_all = []
#for i in range(1234,4322):
#    j = str(i)
#    if j.count("1") == j.count("2") == j.count("3") == j.count("4") == 1:
#        phase_all.append("0" + j)
#for i in range(10234,43211):
#    j = str(i)
#    if j.count("0") == j.count("1") == j.count("2") == j.count("3") == j.count("4"):
#        phase_all.append(j)

max_output = 0
for phase in phase_all:            
    inpt = 0
    for elem_ph in phase:
        lst_copy = lst.copy()
        inpt = run_once(lst_copy, int(elem_ph), inpt)
    if inpt > max_output:
        max_output = inpt
        max_output_phase = phase
print("max_output =", max_output)
print("max_output_phase =", max_output_phase)

