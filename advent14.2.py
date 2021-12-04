import math
from collections import defaultdict

rezept = {}
with open('input14.2test.txt') as f:
    for line in f:
        tuple_line = tuple(((line.replace(",", "")).rstrip()).rsplit(' '))
        rezept[tuple_line[-1]] = (tuple_line[-2],) + tuple_line[:-3:]

print(rezept)

ORE_quantity = 1000000000000
source = {}
for key in rezept:
    if rezept[key][2] == 'ORE':
        source[key] = (int(rezept[key][0]), int(rezept[key][1]))

print(source)

FUEL_rezept = defaultdict(int)            
nnn = [200] * len(source)
for i, key in enumerate(source):
    FUEL_rezept[key] += (nnn[i] // int(rezept[key][1])) * int(rezept[key][0])

print(FUEL_rezept)
