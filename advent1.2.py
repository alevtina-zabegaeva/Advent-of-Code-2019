fuel = 0
with open('input.txt') as f:
    for line in f:
        mass = int(line)
        addition_fuel = mass // 3 - 2
        while addition_fuel > 0:
           fuel += addition_fuel
           addition_fuel = addition_fuel // 3 - 2
print(fuel)
