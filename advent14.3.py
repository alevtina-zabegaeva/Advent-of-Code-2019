import math
from collections import defaultdict

rezept = {}
with open('input14.1.txt') as f:
    for line in f:
        tuple_line = tuple(((line.replace(",", "")).rstrip()).rsplit(' '))
        rezept[tuple_line[-1]] = (tuple_line[-2],) + tuple_line[:-3:]
rezept['ORE'] = ('1', '1', 'ORE')

ore_max = 1000000000000
fuel_0 = ore_max
for k in range(6):
    simple_rezept = defaultdict(int)
    for i in range(1 , len(rezept['FUEL']), 2):
        simple_rezept[rezept['FUEL'][i + 1]] += int(rezept['FUEL'][i])*fuel_0

#    print(simple_rezept)

    for j in range(100):
        keys = []
        for key in simple_rezept:
            keys.append(key)

        for key in keys:
            if rezept[key][2] != 'ORE':
                addition = math.ceil(simple_rezept[key] / int(rezept[key][0]))
                for i in range(1 , len(rezept[key]), 2):
                    simple_rezept[rezept[key][i + 1]] += addition * int(rezept[key][i])
                simple_rezept[key] -= addition * int(rezept[key][0])
#        print(simple_rezept)
#    print()
                
    keys = []
    for key in simple_rezept:
        keys.append(key)

    for key in keys:
        for i in range(1 , len(rezept[key]), 2):
            addition = math.ceil(simple_rezept[key] / int(rezept[key][0]))
            simple_rezept[rezept[key][i + 1]] += (addition * int(rezept[key][i]))
        simple_rezept[key] -= addition * int(rezept[key][0])
#    print(simple_rezept)
    print("f0 =", fuel_0, "f(f0) =", simple_rezept['ORE'], "OREmax - f(f0) =", ore_max - simple_rezept['ORE'])
    fuel_0 = (ore_max * fuel_0) // simple_rezept['ORE']

            
