import copy
import intcode

with open('input25.1.txt') as f:
    lst = list(map(int, f.read().split(',')))

io = intcode.IntCode(lst)
io.evaluate()

vyvod = io.getOutput()
for elem in vyvod:
    print(chr(elem), end = '')

inputs = ['north', 'west',
          'take mug',
          'west',
          'take easter egg',
          'east', 'east', 'south', 'south',
#          'take asterisk',
          'south', 'west', 'north',
#          'take jam',
          'south', 'east', 'north', 'east',
#          'take klein bottle',
          'south', 'west',
#          'take tambourine',
          'west',
#          'take cake',
          'east', 'south', 'east',
#          'take polygon',
          'north', 'inv', 'east']
        
while True:
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

bad_item = set('molten lava', 'escape pod', 'photons', 'infinite loop',
               'giant electromagnet')
good_item = set('asterisk', 'klein bottle', 'tambourine', 'cake', 'polygon',
                'mug', 'easter egg', 'jam')


