import math
from collections import defaultdict

rezept = {}
with open('input14.1.txt') as f:
    for line in f:
        tuple_line = tuple(((line.replace(",", "")).rstrip()).rsplit(' '))
        rezept[tuple_line[-1]] = (tuple_line[-2],) + tuple_line[:-3:]
rezept['ORE'] = ('1', '1', 'ORE')

simple_rezept = defaultdict(int)
for i in range(1 , len(rezept['FUEL']), 2):
    simple_rezept[rezept['FUEL'][i + 1]] += int(rezept['FUEL'][i])

print(simple_rezept)

for j in range(7):
    keys = []
    for key in simple_rezept:
        keys.append(key)

    for key in keys:
        if rezept[key][2] != 'ORE':
            addition = math.ceil(simple_rezept[key] / int(rezept[key][0]))
            for i in range(1 , len(rezept[key]), 2):
                simple_rezept[rezept[key][i + 1]] += addition * int(rezept[key][i])
            simple_rezept[key] -= addition * int(rezept[key][0])
    print(simple_rezept)
print()
            
keys = []
for key in simple_rezept:
    keys.append(key)

for key in keys:
    for i in range(1 , len(rezept[key]), 2):
        simple_rezept[rezept[key][i + 1]] += (math.ceil(simple_rezept[key] /
                                                       int(rezept[key][0])) *
                                              int(rezept[key][i]))
    del simple_rezept[key]
print(simple_rezept)


            
