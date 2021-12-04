from collections import defaultdict
import copy

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

print_map(map2)

def search_way(map3, i_s, j_s):
    map4 = copy.deepcopy(map3)
    map4[i_s][j_s] = '0'
    count = 0
    found = False
    sosedi =((0, 1), (0, -1), (1, 0), (-1, 0))
    while not found:
        count += 1
        addition = set()
        for i, stroka in enumerate(map4):
            for j, elem in enumerate(stroka):
                if elem == '0':
                    for sosed in sosedi:
                        cur_coord = (i + sosed[0], j + sosed[1])
                        cur_sosed = map4[cur_coord[0]][cur_coord[1]]
                        if cur_sosed == '.':
                            addition.add(cur_coord)
                            if cur_coord in w_hier:
                                port = w_hier[cur_coord]
                                if port == 'ZZ':
                                    found = True
                                else:
                                    if w_portals[port][0] == cur_coord:
                                        addition.add(w_portals[port][3])
                                    else:
                                        addition.add(w_portals[port][1])
        for addi in addition:
            map4[addi[0]][addi[1]] = '0'
    print_map(map4)
    return count

w_portals = defaultdict(list)  #where are all the portals
for i in range(len(map2) - 1):
    for j in range(len(map2[i]) - 1):
        if (map2[i][j]).isalpha() and (map2[i][j + 1]).isalpha():
            if j == 0:
                enter = (i, 2)
                exitt = (i, 1)
            elif map2[i][j - 1] == '.':
                enter = (i, j - 1)
                exitt = (i, j)
            else:
                enter = (i, j + 2)
                exitt = (i, j + 1)
            w_portals[map2[i][j] + map2[i][j + 1]].append(enter)
            w_portals[map2[i][j] + map2[i][j + 1]].append(exitt)
        elif (map2[i][j]).isalpha() and (map2[i + 1][j]).isalpha():
            if i == 0:
                enter = (2, j)
                exitt = (1, j)
            elif map2[i - 1][j] == '.':
                enter = (i - 1, j)
                exitt = (i, j)
            else:
                enter = (i + 2, j)
                exitt = (i + 1, j)
            w_portals[map2[i][j] + map2[i + 1][j]].append(enter)
            w_portals[map2[i][j] + map2[i + 1][j]].append(exitt)

#print(w_portals)

w_hier = {}  #what portal is here
for por in w_portals:
    w_hier[w_portals[por][0]] = por
    if por != 'AA' and por != 'ZZ':
        w_hier[w_portals[por][2]] = por

#print(w_hier)

start_i = w_portals['AA'][0][0]
start_j = w_portals['AA'][0][1]
print(search_way(map2, start_i, start_j))
