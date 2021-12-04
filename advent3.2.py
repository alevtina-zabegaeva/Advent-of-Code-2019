with open('input3.1.txt') as f:
    lst1 = list((f.readline().rstrip()).split(','))
    lst2 = list(f.readline().split(','))

def search_extremum(lst, extrem):
    LR = UD = 0
    for i in lst:
        if i[:1] == "R":
            LR += int(i[1:])
            if LR > extrem[1]:
                extrem[1] = LR
        elif i[:1] == "L":
            LR -= int(i[1:])
            if LR < extrem[0]:
                extrem[0] = LR
        elif i[:1] == "U":
            UD += int(i[1:])
            if UD > extrem[3]:
                extrem[3] = UD
        elif i[:1] == "D":
            UD -= int(i[1:])
            if UD < extrem[2]:
                extrem[2] = UD
    return extrem

extremum = [0, 0, 0, 0] # minL = maxR = minD = maxU = 0
extremum = search_extremum(lst1,extremum)
extremum = search_extremum(lst2,extremum)

def array_fill(array, lst, j, k):
    length = 0
    for i in lst:
        if i[:1] == "R":
            for l in range(int(i[1:])):
                j += 1
                length += 1
                if array[j][k] == 0:
                    array[j][k] = length
        elif i[:1] == "L":
            for l in range(int(i[1:])):
                j -= 1
                length += 1
                if array[j][k] == 0:
                    array[j][k] = length
        elif i[:1] == "U":
            for l in range(int(i[1:])):
                k += 1
                length += 1
                if array[j][k] == 0:
                    array[j][k] = length
        elif i[:1] == "D":
            for l in range(int(i[1:])):
                k -= 1
                length += 1
                if array[j][k] == 0:
                    array[j][k] = length
    return array

array1 = [[0] * (extremum[3] - extremum[2] + 1) for i in range(extremum[1] - extremum[0] + 1)]
array1 = array_fill(array1, lst1, - extremum[0], - extremum[2])
array2 = [[0] * (extremum[3] - extremum[2] + 1) for i in range(extremum[1] - extremum[0] + 1)]
array2 = array_fill(array2, lst2, - extremum[0], - extremum[2])

count = max(max(max(i) for i in array1),max(max(i) for i in array2))
for j in range(extremum[1] - extremum[0] + 1):
    for k in range(extremum[3] - extremum[2] + 1):
        if array1[j][k] * array2[j][k] != 0:
            b = array1[j][k] + array2[j][k]
            if count > b:
                 count = b
print(count)
