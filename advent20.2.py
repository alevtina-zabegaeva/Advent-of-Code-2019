from collections import defaultdict
import copy
deep = 80

map2 =[]
with open('input20.1.txt') as f:
    for line in f.readlines(): 
        map2.append(list(line.strip('\n')))

def print_map(map3):
    for m in map3:
        for n in m:
            print(n, end = '')
        print()
    print()

def quant(map3, i, j): #quantity of walls around the element
    count = 0
    if map3[i][j] == "." or map3[i][j] == " " or (map3[i][j]).isupper():
        if map3[i + 1][j] == "#":
            count += 1
        if map3[i - 1][j] == "#":
            count += 1
        if map3[i][j + 1] == "#":
            count += 1
        if map3[i][j - 1] == "#":
            count += 1
    return count

tupik = True    #dead ends filling
while tupik == True:
    tupik = False
    for i in range(1, len(map2) - 1):
        for j in range(1, len(map2[i]) - 1):
            if quant(map2, i, j) > 2:
                map2[i][j] = '#'
                tupik = True

#print_map(map2)

def search_way(map0, i_s, j_s):
    map4 = [copy.deepcopy(map0) for x in range(deep)]
    map4[0][i_s][j_s] = '0'
    addition0 = [set() for x in range(deep)]
    (addition0[0]).add((i_s, j_s))
    for key in inn_portals:
        map4[-1][inn_portals[key][0][0]][inn_portals[key][0][1]] = '#'
    for key in out_portals:
        if key != 'AA' and key != 'ZZ':
            map4[0][out_portals[key][0][0]][out_portals[key][0][1]] = '#'
    for i_m in range(1, deep):
        map4[i_m][out_portals['AA'][0][0]][out_portals['AA'][0][1]] = '#'
        map4[i_m][out_portals['ZZ'][0][0]][out_portals['ZZ'][0][1]] = '#'
    count = 0
    found = False
    sosedi =((0, 1), (0, -1), (1, 0), (-1, 0))
    while not found:
        count += 1
        addition = [set() for x in range(deep)]
        for lev, labir in enumerate(addition0):
            for a in labir:
                for sosed in sosedi:
                    cur_coord = (a[0] + sosed[0], a[1] + sosed[1])
                    cur_sosed = map4[lev][cur_coord[0]][cur_coord[1]]
                    if cur_sosed == '.':
                        (addition[lev]).add(cur_coord)
                        if cur_coord in out_hier:
                            port = out_hier[cur_coord]
                            if port == 'ZZ':
                                found = True
                            else:
                                (addition[lev - 1]).add(inn_portals[port][1])
                        elif cur_coord in inn_hier:
                            port = inn_hier[cur_coord]
                            (addition[lev + 1]).add(out_portals[port][1])                                            
        for y, addit in enumerate(addition):
            for addi in addit:
                map4[y][addi[0]][addi[1]] = '0'
            addition0[y] = addit.copy()
    return count

out_portals = defaultdict(list)  #where are all the portals
inn_portals = defaultdict(list)
for i in range(len(map2) - 1):
    for j in range(len(map2[i]) - 1):
        if (map2[i][j]).isalpha() and (map2[i][j + 1]).isalpha():
            if j == 0:
                out_portals[map2[i][j] + map2[i][j + 1]].append((i, 2))
                out_portals[map2[i][j] + map2[i][j + 1]].append((i, 1))
            elif j == len(map2[i]) - 2:
                out_portals[map2[i][j] + map2[i][j + 1]].append((i, j - 1))
                out_portals[map2[i][j] + map2[i][j + 1]].append((i, j))                
            elif map2[i][j - 1] == '.':
                inn_portals[map2[i][j] + map2[i][j + 1]].append((i, j - 1))
                inn_portals[map2[i][j] + map2[i][j + 1]].append((i, j))
            else:
                inn_portals[map2[i][j] + map2[i][j + 1]].append((i, j + 2))
                inn_portals[map2[i][j] + map2[i][j + 1]].append((i, j + 1))
        elif (map2[i][j]).isalpha() and (map2[i + 1][j]).isalpha():
            if i == 0:
                out_portals[map2[i][j] + map2[i + 1][j]].append((2, j))
                out_portals[map2[i][j] + map2[i + 1][j]].append((1, j))
            elif i == len(map2) - 2:
                out_portals[map2[i][j] + map2[i + 1][j]].append((i - 1, j))
                out_portals[map2[i][j] + map2[i + 1][j]].append((i, j))                
            elif map2[i - 1][j] == '.':
                inn_portals[map2[i][j] + map2[i + 1][j]].append((i - 1, j))
                inn_portals[map2[i][j] + map2[i + 1][j]].append((i, j))
            else:
                inn_portals[map2[i][j] + map2[i + 1][j]].append((i + 2, j))
                inn_portals[map2[i][j] + map2[i + 1][j]].append((i + 1, j))
                
out_hier = {}  #what portal is here
for por in out_portals:
    out_hier[out_portals[por][0]] = por
inn_hier = {}
for por in inn_portals:
    inn_hier[inn_portals[por][0]] = por

start_i = out_portals['AA'][0][0]
start_j = out_portals['AA'][0][1]
print(search_way(map2, start_i, start_j))
