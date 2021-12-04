#input:
with open('input16.1.txt') as f:
    array1 = tuple(map(int, f.read()))

#example 1:
#array1 = tuple(map(int, "12345678"))

#example 2:
#array1 = tuple(map(int, "80871224585914546619083218645595"))

#example 3:
#array1 = tuple(map(int, "19617804207202209144916044189917"))

#example 4:
#array1 = tuple(map(int, "69317163492948606335995924319873"))

pat0 = (0, 1, 0, -1)

for k in range(100):
    array2 = []
    for i in range(len(array1)):
        summ = 0
        for j, element in enumerate(array1):
    #        index = ((j + 1) // (i + 1)) % 4
    #        pattern = pat0[index]
            summ += pat0[((j + 1) // (i + 1)) % 4]*element
    #        print(element, '*', pattern, ' + ', end = ' ')
    #    print('= ', summ, ' = ', abs(summ) % 10)    
        array2.append(abs(summ) % 10)
    array1 = tuple(array2.copy())

print(array2)
for i in range(8):
    print(array2[i], end = '')

