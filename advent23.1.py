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
while not end:
    inp = [False for j in range(50)]
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
                end = True
                print(c)
                break
            inp[a] = True
            io[a].addInput([b, c])
    for i in range(50):
        if not inp[i]:
            io[i].addInput([-1])
        io[i].evaluate()

