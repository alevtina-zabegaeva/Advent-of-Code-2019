with open('input10.1.txt') as f:
    map1 = f.read().splitlines()

#with open('input10.1test.txt') as f:
#    map2 = [list(line.strip()) for line in f]
    
#print(map1)
#print(map2)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

count = []
count_num = 0
for i in range(len(map1)):
    spisok_i = []
    for j in range(len(map1[1])):
        spisok_i.append(0)
        if map1[i][j] == ".":
            continue
        for k in range(len(map1)):
#            visible_str = ""
            for l in range(len(map1[1])):
                if map1[k][l] == "." or k == i and l == j:
#                    visible_str += "."
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
#                        visible_str += "0"
                        break
                if visible:
                    spisok_i[j] += 1
                    if spisok_i[j] > count_num:
                        count_num = spisok_i[j]
#                    visible_str += "1"
#            print(i, j, visible_str)
    count.append(spisok_i)
    
#for i in count:
#    print(i)
print(count_num)

