n = int(input())

tank_capacity = 255
poured_water = 0

for _ in range(n):
    liters_of_water = int(input())
    if poured_water + liters_of_water <= tank_capacity:
        poured_water += liters_of_water
    else:
        print("Insufficient capacity!")

print(poured_water)
