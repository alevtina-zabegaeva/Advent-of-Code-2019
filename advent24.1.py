import copy

lst = []
with open('input24.1.txt') as f:
    lst = [line.strip('\n') + '.' for line in f.readlines()]
lst.append('.' * len(lst[-1]))

for st in lst:
    print(st)
print()

def zh(lst, i, j):
    sosed = ((0, 1), (0, -1), (1, 0), (-1, 0))
    counter = 0
    for curr in sosed:
        if lst[i + curr[0]][j + curr[1]] == '#':
            counter += 1
    return counter

def rating(lst):
    r = 0
    for i in range(len(lst) - 1):
        for j in range(len(lst[i]) - 1):
            if lst[i][j] == '#':
                r += 2 ** (i * (len(lst[i]) - 1) + j)
    return r

steps = []
steps.append(copy.deepcopy(lst))
end = False
while not end:
    lst_next = set()
    for i in range(len(lst) - 1):
        for j in range(len(lst[i]) - 1):
            q = zh(lst, i, j)
            el = lst[i][j]
            if el == '#' and q != 1 or el == '.' and (q == 1 or q == 2):
                lst_next.add((i, j))
    for ch in lst_next:
        if lst[ch[0]][ch[1]] == '#':
            lst[ch[0]] = lst[ch[0]][:ch[1]] + '.' + lst[ch[0]][ch[1] + 1:]
        else:
            lst[ch[0]] = lst[ch[0]][:ch[1]] + '#' + lst[ch[0]][ch[1] + 1:]
    if lst in steps:
        end = True
    else:
        steps.append(copy.deepcopy(lst))
    for st in lst:
        print(st)
    print()

print(rating(lst))
