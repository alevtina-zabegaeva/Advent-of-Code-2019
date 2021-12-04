import copy

def lcm(a, b):
    m = a * b
    while b:
        a, b = b, a % b
    return m // a

#       Io,         Europa,      Ganymede,    Callisto
#input:
pos = [[14, 4, 5], [12, 10, 8], [1, 7, -10], [16, -5, 3]]

#example 1:
#pos = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]

#example 2:
#pos = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]

vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
pos_start = copy.deepcopy(pos)

period = [0, 0, 0]
step = 0

while 0 in period:
    step += 1
    equal = [True, True, True]
    
    #apply gravity:
    for i, pos_moon1 in enumerate(pos):
        for j, pos_moon2 in enumerate(pos):
            if i <= j:
                continue
            for k in range(3):
                if pos_moon1[k] < pos_moon2[k]:
                    vel[i][k] += 1
                    vel[j][k] -= 1
                elif pos_moon1[k] > pos_moon2[k]:
                    vel[i][k] -= 1
                    vel[j][k] += 1

    #apply velocity:
    for i in range(4):
        for j in range(3):
            pos[i][j] += vel[i][j]
            equal[j] = equal[j] and (vel[i][j] == 0) and (pos[i][j] == pos_start[i][j])

    for j in range(3):
        if period[j] == 0 and equal[j] == True:
            period[j] = step

print(lcm(lcm(period[0], period[1]), period[2]))
