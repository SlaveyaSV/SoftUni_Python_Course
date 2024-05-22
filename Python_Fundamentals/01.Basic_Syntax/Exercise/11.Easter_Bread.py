budget = float(input())
flour_price_per_kg = float(input())

eggs_price_per_kg = 0.75 * flour_price_per_kg
milk_per_250_ml = flour_price_per_kg * (1 + 0.25) / 4
bread_price = flour_price_per_kg + eggs_price_per_kg + milk_per_250_ml

coloured_eggs = 0
bread_count = 0

while budget >= bread_price:
    budget -= bread_price
    bread_count += 1
    coloured_eggs += 3

    if bread_count % 3 == 0:
        coloured_eggs -= (bread_count-2)

print(f"You made {bread_count} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
