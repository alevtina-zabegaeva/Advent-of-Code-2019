with open('input6.1.txt') as f:
    map1 = f.read().splitlines()
dict1 = []
map2 = []
for i in range(len(map1)):
    a = map1[i].split(")")
    map1[i] = a[0]
    map2.append(a[1])
    for j in a:
        if dict1.count(j) == 0:
            dict1.append(j)
print("map1 =", map1)
print("map2 =", map2)
print("dict =",dict1)

count_array = []
count = 0
for elem in dict1:
    count_array.append(0)
    while map2.count(elem) != 0:
        elem = map1[map2.index(elem)]
        count += 1
        count_array[-1] += 1
print(count_array)
print(count)

            
