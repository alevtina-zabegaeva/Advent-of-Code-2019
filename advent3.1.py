with open('input3.1.txt') as f:
    lst1 = list((f.readline().rstrip()).split(','))
    lst2 = list(f.readline().split(','))

minL = maxR = minD = maxU = 0
LR = UD = 0
for i in lst1:
    if i[:1] == "R":
        LR += int(i[1:])
        if LR > maxR:
            maxR = LR
    elif i[:1] == "L":
        LR -= int(i[1:])
        if LR < minL:
            minL = LR
    elif i[:1] == "U":
        UD += int(i[1:])
        if UD > maxU:
            maxU = UD
    elif i[:1] == "D":
        UD -= int(i[1:])
        if UD < minD:
            minD = UD
    else:
        print("Error!")
        break
LR = UD = 0
for i in lst2:
    if i[:1] == "R":
        LR += int(i[1:])
        if LR > maxR:
            maxR = LR
    elif i[:1] == "L":
        LR -= int(i[1:])
        if LR < minL:
            minL = LR
    elif i[:1] == "U":
        UD += int(i[1:])
        if UD > maxU:
            maxU = UD
    elif i[:1] == "D":
        UD -= int(i[1:])
        if UD < minD:
            minD = UD
    else:
        print("Error!")
        break
print(minL, maxR, minD, maxU)    

j = - minL
k = - minD
array1 = [[False] * (maxU - minD + 1) for i in range(maxR - minL + 1)]
for i in lst1:
    if i[:1] == "R":
        for l in range(int(i[1:])):
            j += 1
            array1[j][k] = True
    elif i[:1] == "L":
        for l in range(int(i[1:])):
            j -= 1
            array1[j][k] = True
    elif i[:1] == "U":
        for l in range(int(i[1:])):
            k += 1
            array1[j][k] = True
    elif i[:1] == "D":
        for l in range(int(i[1:])):
            k -= 1
            array1[j][k] = True
    else:
        print("Error!")
        break

j = - minL
k = - minD
array2 = [[False] * (maxU - minD + 1) for i in range(maxR - minL + 1)]
for i in lst2:
    if i[:1] == "R":
        for l in range(int(i[1:])):
            j += 1
            array2[j][k] = True
    elif i[:1] == "L":
        for l in range(int(i[1:])):
            j -= 1
            array2[j][k] = True
    elif i[:1] == "U":
        for l in range(int(i[1:])):
            k += 1
            array2[j][k] = True
    elif i[:1] == "D":
        for l in range(int(i[1:])):
            k -= 1
            array2[j][k] = True
    else:
        print("Error!")
        break

count = maxU - minD + 1 + maxR - minL + 1
for j in range(maxR - minL + 1):
    for k in range(maxU - minD + 1):
        if array1[j][k] * array2[j][k] == 1:
            b = abs(minL + j) + abs(minD + k)
            if count > b:
                 count = b
print(count)
