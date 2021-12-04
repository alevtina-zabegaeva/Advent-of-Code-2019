with open('input2.txt') as f:
    lst = list(map(int, f.read().split(',')))
lst[1]=12
lst[2]=2
for i in range(0,len(lst),4):
    if lst[i]==1:
        lst[lst[i+3]]=lst[lst[i+1]]+lst[lst[i+2]]
    elif lst[i]==2:
        lst[lst[i+3]]=lst[lst[i+1]]*lst[lst[i+2]]
    elif lst[i]==99:
        break
    else:
        print('Error!')
        break
print(lst)

