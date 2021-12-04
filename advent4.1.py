start = 206938
finish = 679128
count = 0

for number in range(start, finish + 1):
    increasing = True
    double = False
    number_str = str(number)
    for i in range(5):
        if int(number_str[i]) > int(number_str[i+1]):
            increasing = False
            break
        if number_str[i] == number_str[i+1]:
            double = True
    if increasing * double == True:
        count += 1
print(count)
        
