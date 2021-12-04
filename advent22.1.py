lst = []
with open('input22.1.txt') as f:
    lst = [line.strip('\n') for line in f.readlines()]

#print(lst)
stack = list(range(10007))
#stack = list(range(10))

def deal(stack1):
    stack2 = stack1.copy()
    stack2.reverse()
    return stack2

def deal_inc(stack1, inc):
    stack2 = [-1] * len(stack1)
    for i in range(len(stack1)):
        stack2[(i * inc) % len(stack1)] = stack1[i]
    return stack2

def cut(stack1, N):
    return stack1[N:] + stack1[:N]

for command in lst:
    if command[:3] == 'cut':
        stack2 = cut(stack, int(command[4:]))
    elif command[-1:].isdigit():
        stack2 = deal_inc(stack, int(command[20:]))
    else:
        stack2 = deal(stack)
    stack = stack2.copy()

print(stack.index(2019))
