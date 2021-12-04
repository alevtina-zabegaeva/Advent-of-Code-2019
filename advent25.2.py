import intcode2
from collections import defaultdict

with open('input25.1.txt') as f:
    lst_list = list(map(int, f.read().split(',')))
lst = defaultdict(int)
for key, value in enumerate(lst_list):
    lst[key] = value

io = intcode2.IntCode(lst)
io.evaluate()

vyvod = io.getOutput()
for elem in vyvod:
    print(chr(elem), end = '')

inputs = ['north', 'west',
          'take mug',
          'west',
          'take easter egg',
          'east', 'east', 'south', 'south',
          'take asterisk',
          'south', 'west', 'north',
          'take jam',
          'south', 'east', 'north', 'east',
          'take klein bottle',
          'south', 'west',
          'take tambourine',
          'west',
          'take cake',
          'east', 'south', 'east',
          'take polygon',
          'north', 'inv', 'east']
        
while len(inputs) != 0:
    vvod = inputs.pop(0)
    inp_lst = []
    for elem in vvod:
        inp_lst.append(ord(elem))
    inp_lst.append(10)

    io.addInput(inp_lst)
    io.evaluate()

    vyvod = io.getOutput()

for elem in vyvod:
    if elem > 127:
        print(elem, end = '')
    else:
        print(chr(elem), end = '')

bad = ('molten lava', 'escape pod', 'photons', 'infinite loop',
               'giant electromagnet')
good = {0:'asterisk', 1:'klein bottle', 2:'tambourine', 3:'cake',
             4:'polygon', 5:'mug', 6:'easter egg', 7:'jam'}

for i0 in ('drop ' + good[0], 'take ' + good[0]):
    for i1 in ('drop ' + good[1], 'take ' + good[1]):
        for i2 in ('drop ' + good[2], 'take ' + good[2]):
            for i3 in ('drop ' + good[3], 'take ' + good[3]):
                for i4 in ('drop ' + good[4], 'take ' + good[4]):
                    for i5 in ('drop ' + good[5], 'take ' + good[5]):
                        for i6 in ('drop ' + good[6], 'take ' + good[6]):
                            for i7 in ('drop ' + good[7], 'take ' + good[7]):
                                for elem in vyvod:
                                    if elem > 127:
                                        print(elem, end = '')
                                    else:
                                        print(chr(elem), end = '')
                                inputs = [i0, i1, i2, i3, i4, i5, i6, i7, 'east']
                                while len(inputs) != 0:
                                    vvod = inputs.pop(0)
                                    inp_lst = []
                                    for elem in vvod:
                                        inp_lst.append(ord(elem))
                                    inp_lst.append(10)

                                    io.addInput(inp_lst)
                                    io.evaluate()

                                    vyvod = io.getOutput()
