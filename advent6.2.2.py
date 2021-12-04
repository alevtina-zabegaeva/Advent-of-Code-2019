with open('input6.1.txt') as f:
    map1 = f.read().splitlines()

map2 = []
dic1 = {}
for i in range(len(map1)):
    a = map1[i].split(")")
    map1[i] = a[0]
    map2.append(a[1])
    dic1[a[1]] = a[0]

#print("map1 =", map1)
#print("map2 =", map2)

def find_route(elem, array1, array2):
    route = []
    while elem != "COM":
        elem = array1[array2.index(elem)]
        route.append(elem)
    return route

def find_rout2(elem, d):
    route = []
    while d[elem] != 'COM':
        route.append(elem)
        elem = d[elem]
    return route

routeYOU = find_route("YOU", map1, map2)
routeSAN = find_route("SAN", map1, map2)

for i in range(len(routeYOU)):
    if routeSAN.count(routeYOU[i]) != 0:
        length = i + routeSAN.index(routeYOU[i])
        break
print("length =", length)
#print("routeYOU =", routeYOU)
#print("routeSAN =", routeSAN)
