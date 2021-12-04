wide = 25
tall = 6
layer_length = wide * tall
with open('input8.1.txt') as f:
    file_str = str(f.read())

layer_all = []
count0min = layer_length
for i in range(len(file_str) // (layer_length)):
    layer = []
    count0 = 0
    count1 = 0
    count2 = 0
    for j in range(tall):
        stroka = file_str[(i*layer_length + j*wide):(i*layer_length + (j+1)*wide)]
        layer.append(stroka)
        count0 += stroka.count("0")
        count1 += stroka.count("1")
        count2 += stroka.count("2")
    if count0 < count0min:
        count0min = count0
        layer0min = i
        x = count1 * count2
    layer_all.append(layer)
print(count0min, layer0min, x)

