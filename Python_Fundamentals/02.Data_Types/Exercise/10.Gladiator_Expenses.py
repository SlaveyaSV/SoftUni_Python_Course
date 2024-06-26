count_of_lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
broken_shield_count = 0

for lost_fight in range(1, count_of_lost_fights+1):

    if lost_fight % 2 == 0:
        expenses += helmet_price

    if lost_fight % 3 == 0:
        expenses += sword_price
        if lost_fight % 2 == 0:
            expenses += shield_price
            broken_shield_count += 1

    if broken_shield_count == 2:
        expenses += armor_price
        broken_shield_count = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")
