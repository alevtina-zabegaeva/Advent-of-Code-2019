#       Io,         Europa,      Ganymede,    Callisto
#input:
pos = [[14, 4, 5], [12, 10, 8], [1, 7, -10], [16, -5, 3]]

#example 1:
#pos = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]

#example 2:
#pos = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]

vel = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for step in range(1000):
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

#total energy in the system calculation:
total = 0
for i in range(4):
    pot = 0
    kin = 0
    for j in range(3):
        pot += abs(pos[i][j])
        kin += abs(vel[i][j])
    total += pot*kin

print(pos)
print(vel)
print(total)
