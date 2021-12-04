wide = 25
tall = 6
layer_length = wide * tall
with open('input8.1.txt') as f:
    file_str = str(f.read())

layer_all = []
for i in range(len(file_str) // (layer_length)):
    layer = []
    for j in range(tall):
        stroka = file_str[(i*layer_length + j*wide):(i*layer_length + (j+1)*wide)]
        layer.append(stroka)
    layer_all.append(layer)

c = "2" * wide
picture = [c for j in range(tall)]

for i in range(len(layer_all)):
    for j in range(tall):
        for k in range(wide):
            if picture[j][k] == "2":
                picture[j] = picture[j][:k] + layer_all[i][j][k] + picture[j][k+1:]

for j in range(tall):
    print(picture[j])
