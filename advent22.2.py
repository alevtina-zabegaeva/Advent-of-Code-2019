lst = []
with open('input22.1.txt') as f:
    lst = [line.strip('\n') for line in f.readlines()]

#length = 10007
length = 119315717514047
times = 101741582076661

def bezu(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)

def deal(length):
    return -1, length - 1

def deal_inc(length, inc):
    return inc, 0

def cut(length, N):
    return 1, -N

A1 = 1
B1 = 0
for command in lst:
    if command[:3] == 'cut':
        A2, B2 = cut(length, int(command[4:]))
    elif command[-1:].isdigit():
        A2, B2 = deal_inc(length, int(command[20:]))
    else:
        A2, B2 = deal(length)
    A1, B1 = (A1*A2)%length, (B1*A2 + B2)%length

a, b = [], []
times2 = bin(times)
print(times2)
for i in range(1, len(times2) - 1):
    if int(times2[-i]):
        a.append(A1)
        b.append(B1)
    A1, B1 = (A1*A1)%length, (B1*A1 + B1)%length
    i += 1
A1, B1 = a[0], b[0]
for i in range(1, len(a)):
    A1, B1 = (A1*a[i])%length, (B1*a[i] + b[i])%length
print(2020, (bezu(A1, length)[0])*(2020 - B1) % length)
