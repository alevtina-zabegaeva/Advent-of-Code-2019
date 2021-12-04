import math

with open('input10.1.txt') as f:
    map1 = f.read().splitlines()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

i = 11
j = 11
#visible_map = []
visible_lst = []
for k in range(len(map1)):
    visible_str = ""
    for l in range(len(map1[1])):
        if map1[k][l] == "." or k == i and l == j:
#            visible_str += "."
            continue
        delta_i = i - k
        delta_j = j - l
        nod = abs(gcd(delta_i, delta_j))
        step_i = int(delta_i / nod)
        step_j = int(delta_j / nod)
        visible = True
        for m in range(1,abs(nod)):
            if map1[k + step_i*m][l + step_j*m] == "#":
                visible = False
#                visible_str += "0"
                break
        if visible:
#            visible_str += "1"
            visible_lst.append([round(math.atan2(delta_j,-delta_i),5), k, l])
#    visible_map.append(visible_str)

#for i in visible_map:
#    print(i)
visible_lst.sort()
print(visible_lst[198], visible_lst[198][2]*100 + visible_lst[198][1])


   

