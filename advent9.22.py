import copy
import intcode

with open('input9.1.txt') as f:
    lst = list(map(int, f.read().split(',')))

io = intcode.IntCode(lst)
io.addInput([1])
io.evaluate()
print(io.getOutput())
