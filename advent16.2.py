#input:
with open('input16.1.txt') as f:
    st = f.read()
array1 = tuple([int(item) for item in st])

#example 1:
#st = "03036732577212944063491565474664"
#array1 = tuple([int(item) for item in st])

#example 2:
#st = "02935109699940807407585447034323"
#array1 = [int(item) for item in st]

#example 3:
#st = "03081770884921959731165446850517"
#array1 = [int(item) for item in st]

leng = len(st)  #650, 32
offset = int(st[:7]) #5971509, 303673

new_len = leng*10000 - offset #528492
start = leng - new_len % leng #608
array2 = tuple(list(array1[start:]) + (new_len // leng) * list(array1))

for k in range(100):
    array3 = []
    array3 = [sum(array2) % 10]
    for i in range(1, len(array2)):
        array3.append((array3[i - 1] - array2[i - 1]) % 10)
    array2 = tuple(array3.copy())
    print(array2[:8])
