decorations_qty_per_shopping = int(input())
days_until_christmas = int(input())

total_cost = 0
gained_spirit = 0

for day in range(1, days_until_christmas+1):
    if day % 11 == 0:
        decorations_qty_per_shopping += 2

    if day % 2 == 0:
        total_cost += decorations_qty_per_shopping * 2
        gained_spirit += 5

    if day % 3 == 0:
        total_cost += decorations_qty_per_shopping * (5+3)
        gained_spirit += (3+10)

    if day % 5 == 0:
        total_cost += decorations_qty_per_shopping * 15
        gained_spirit += 17

    if day % 3 == 0 and day % 5 == 0:
        gained_spirit += 30

    if day % 10 == 0:
        gained_spirit -= 20
        total_cost += (5+3+15)
        if day == days_until_christmas:
            gained_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {gained_spirit}")
