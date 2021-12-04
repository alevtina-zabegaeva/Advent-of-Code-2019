from collections import defaultdict
import copy

def search_elem(map3, elem):
    for i, m in enumerate(map3):
        for j, n in enumerate(m):
            if n == elem:
                return i, j

map2 =[]
with open('input18.1.txt') as f:
    for line in f.readlines(): 
        map2.append(list(line.strip()))

i_start, j_start = search_elem(map2, '@') #changing of the center square
map2[i_start - 1][j_start - 1] = '@'
map2[i_start + 1][j_start - 1] = '@'
map2[i_start - 1][j_start + 1] = '@'
map2[i_start + 1][j_start + 1] = '@'
map2[i_start - 1][j_start] = '#'
map2[i_start + 1][j_start] = '#'
map2[i_start][j_start - 1] = '#'
map2[i_start][j_start + 1] = '#'
map2[i_start][j_start] = '#'
i_start = (i_start - 1, i_start + 1, i_start + 1, i_start - 1)
j_start = (j_start - 1, j_start - 1, j_start + 1, j_start + 1)

def print_map(map3):
    for m in map3:
        for n in m:
            print(n, end = '')
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

def search_keys(map3, i_s, j_s, keys1):
    map4 = copy.deepcopy(map3)
    map4[i_s][j_s] = '0'
    count = 0
    end = False
    sosedi =((0, 1), (0, -1), (1, 0), (-1, 0))
    return_keys1 = {}
    while not end:
        count += 1
        end = True
        addition = set()
        for i, stroka in enumerate(map4):
            for j, elem in enumerate(stroka):
                if elem == '0':
                    for sosed in sosedi:
                        cur_sosed = map4[i + sosed[0]][j + sosed[1]]
                        if cur_sosed.lower() in keys1:
                            addition.add((i + sosed[0], j + sosed[1]))
                            end = False
                        elif cur_sosed.islower() and not cur_sosed in return_keys1:
                            return_keys1[cur_sosed] = count
        for addi in addition:
            map4[addi[0]][addi[1]] = '0'
    return return_keys1

w_keys ={}  #where are all the keys
for i, m in enumerate(map2):
    for j, n in enumerate(m):
        if n.islower():
            w_keys[n] = (i, j)

for i in range(4):
    map2[i_start[i]][j_start[i]] = '.'

tree0 = {}  #collected keys, distance, next potential keys
tree0[('.')] = [0, search_keys(map2, i_start[0], j_start[0], ['.']),
                    search_keys(map2, i_start[1], j_start[1], ['.']),
                    search_keys(map2, i_start[2], j_start[2], ['.']),
                    search_keys(map2, i_start[3], j_start[3], ['.']),
                i_start[0], j_start[0], i_start[1], j_start[1],
                i_start[2], j_start[2], i_start[3], j_start[3]]

for e in tree0:
    print("tree0[", e, "] = ", tree0[e], sep='', end ='')
print()

for perebor in range(len(w_keys)):
    tree = {}   #next steps
    for subt in tree0:
        for elem in tree0[subt][1]:    
            k, l = w_keys[elem][0], w_keys[elem][1]
            keys_n = list(copy.copy(subt))
            keys_n.append(elem)
            keys_n = tuple(keys_n)
            tree[keys_n] = [tree0[subt][1][elem] + tree0[subt][0],
                            search_keys(map2, k, l, keys_n),
                            search_keys(map2, tree0[subt][7], tree0[subt][8], keys_n),
                            search_keys(map2, tree0[subt][9], tree0[subt][10], keys_n),
                            search_keys(map2, tree0[subt][11], tree0[subt][12], keys_n),
                            k, l,
                            tree0[subt][7], tree0[subt][8],
                            tree0[subt][9], tree0[subt][10],
                            tree0[subt][11], tree0[subt][12]]
        for elem in tree0[subt][2]:    
            k, l = w_keys[elem][0], w_keys[elem][1]
            keys_n = list(copy.copy(subt))
            keys_n.append(elem)
            keys_n = tuple(keys_n)
            tree[keys_n] = [tree0[subt][2][elem] + tree0[subt][0],
                            search_keys(map2, tree0[subt][5], tree0[subt][6], keys_n),
                            search_keys(map2, k, l, keys_n),
                            search_keys(map2, tree0[subt][9], tree0[subt][10], keys_n),
                            search_keys(map2, tree0[subt][11], tree0[subt][12], keys_n),
                            tree0[subt][5], tree0[subt][6],
                            k, l,
                            tree0[subt][9], tree0[subt][10],
                            tree0[subt][11], tree0[subt][12]]
        for elem in tree0[subt][3]:    
            k, l = w_keys[elem][0], w_keys[elem][1]
            keys_n = list(copy.copy(subt))
            keys_n.append(elem)
            keys_n = tuple(keys_n)
            tree[keys_n] = [tree0[subt][3][elem] + tree0[subt][0],
                            search_keys(map2, tree0[subt][5], tree0[subt][6], keys_n),
                            search_keys(map2, tree0[subt][7], tree0[subt][8], keys_n),
                            search_keys(map2, k, l, keys_n),
                            search_keys(map2, tree0[subt][11], tree0[subt][12], keys_n),
                            tree0[subt][5], tree0[subt][6],
                            tree0[subt][7], tree0[subt][8],
                            k, l,
                            tree0[subt][11], tree0[subt][12]]
        for elem in tree0[subt][4]:    
            k, l = w_keys[elem][0], w_keys[elem][1]
            keys_n = list(copy.copy(subt))
            keys_n.append(elem)
            keys_n = tuple(keys_n)
            tree[keys_n] = [tree0[subt][4][elem] + tree0[subt][0],
                            search_keys(map2, tree0[subt][5], tree0[subt][6], keys_n),
                            search_keys(map2, tree0[subt][7], tree0[subt][8], keys_n),
                            search_keys(map2, tree0[subt][9], tree0[subt][10], keys_n),
                            search_keys(map2, k, l, keys_n),
                            tree0[subt][5], tree0[subt][6],
                            tree0[subt][7], tree0[subt][8],
                            tree0[subt][9], tree0[subt][10],
                            k, l]   
    to_delete = set()   #to delete slower ways
    byl = set()
    for ke1 in tree:
        for ke2 in tree:
            if not(ke2 in byl):
                a = list(ke1)
                a.sort()
                b = list(ke2)
                b.sort()
                if (tree[ke1][5] == tree[ke2][5] and tree[ke1][6] == tree[ke2][6] and
                    tree[ke1][7] == tree[ke2][7] and tree[ke1][8] == tree[ke2][8] and
                    tree[ke1][9] == tree[ke2][9] and tree[ke1][10] == tree[ke2][10] and
                    tree[ke1][11] == tree[ke2][11] and tree[ke1][12] == tree[ke2][12] and
                    ke1 != ke2 and a == b):
                    if tree[ke1][0] < tree[ke2][0]:
                        to_delete.add(ke2)
                    else:
                        to_delete.add(ke1)
        byl.add(ke1)        
                        
    for elem in to_delete:
        tree.pop(elem)

    for e in tree:
        print("tree0[", e, "] = ", tree[e], sep='')
    print()
    tree0 = copy.deepcopy(tree)

