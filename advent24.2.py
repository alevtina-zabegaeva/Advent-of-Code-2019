import copy
deep = 200

#example
##lst =  [['.', '.', '.', '.', '#'],
##        ['#', '.', '.', '#', '.'],
##        ['#', '.', '?', '#', '#'],
##        ['.', '.', '#', '.', '.'],
##        ['#', '.', '.', '.', '.']]
#input
lst =  [['.', '.', '#', '.', '#'],
        ['#', '#', '#', '#', '#'],
        ['.', '#', '?', '.', '.'],
        ['.', '.', '.', '#', '.'],
        ['#', '#', '.', '.', '.']]
lst0 = [['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '?', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.']]

level = []
for i in range(deep // 2):
    level.append(copy.deepcopy(lst0))
level.append(lst)
for i in range(deep // 2):
    level.append(copy.deepcopy(lst0))

def zh(level, i, j, l):
    counter = 0
    #upper
    if i == 0: 
        if l != 0 and level[l - 1][1][2] == '#':
                counter += 1
    elif level[l][i - 1][j] == '#':
            counter += 1
    elif level[l][i - 1][j] == '?' and l != deep:
        for k in range(5):
            if level[l + 1][4][k] == '#':
                counter += 1
    #lower
    if i == 4:
        if l != 0 and level[l - 1][3][2] == '#':
            counter += 1
    elif level[l][i + 1][j] == '#':
            counter += 1
    elif level[l][i + 1][j] == '?' and l != deep:
        for k in range(5):
            if level[l + 1][0][k] == '#':
                counter += 1
    #left
    if j == 0:
        if l != 0 and level[l - 1][2][1] == '#':
            counter += 1
    elif level[l][i][j - 1] == '#':
            counter += 1
    elif level[l][i][j - 1] == '?' and l != deep:
        for k in range(5):
            if level[l + 1][k][4] == '#':
                counter += 1                
    #right
    if j == 4:
        if l != 0 and level[l - 1][2][3] == '#':
            counter += 1
    elif level[l][i][j + 1] == '#':
            counter += 1
    elif level[l][i][j + 1] == '?' and l != deep:
        for k in range(5):
            if level[l + 1][k][0] == '#':
                counter += 1
            
    return counter

##for l in level:
##    for st in l:
##        for e in st:
##            print(e, end = '')
##        print()
##    print()
##print()

quan = 0
for l in level:
    for st in l:
        quan += st.count('#')
            
for step in range(deep):
    nex = copy.deepcopy(level)
    for l in range(deep + 1):
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                q = zh(level, i, j, l)
                el = level[l][i][j]
                if el == '#' and q != 1:
                    nex[l][i][j] = '.'
                    quan -= 1
                if el == '.' and (q == 1 or q == 2):
                    nex[l][i][j] = '#'
                    quan += 1

    level = copy.deepcopy(nex)
    print(quan)
##    for l in level:
##        for st in l:
##            for e in st:
##                print(e, end = '')
##            print()
##        print()
##    print()
