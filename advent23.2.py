import copy
import intcode

with open('input23.1.txt') as f:
    lst = list(map(int, f.read().split(',')))

io = []

for i in range(50):
    io.append(intcode.IntCode(lst))
    io[i].addInput([i])
    io[i].evaluate()

end = False
idle = 0
Y = -1
while not end:
    inp = [False] * 50
    for i in range(50):
        a1 = io[i].getOutput()
        while True:
            try:
                a = a1.pop(0)
            except IndexError:
                break
            b = a1.pop(0)
            c = a1.pop(0)
            if a == 255:
                NAT = (b, c)
            else:
                inp[a] = True
                io[a].addInput([b, c])
    if not(True in inp):
        idle += 1
    else:
        idle = 0
    if idle == 2:    
        io[0].addInput([NAT[0]])
        io[0].addInput([NAT[1]])
        inp[0] = True
        idle = 0
        print(NAT)
        if NAT[1] == Y:
            end = True
            print('End!', NAT)
            break
        else:
            Y = NAT[1]
    for i in range(50):
        if not inp[i]:
            io[i].addInput([-1])
        io[i].evaluate()
