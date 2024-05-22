number_of_orders = int(input())

total_price = 0

for order in range(1, number_of_orders+1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100.00:
        if 1 <= days <= 31:
            if 1 <= capsules_per_day <= 2000:
                price = price_per_capsule * days * capsules_per_day
                total_price += price
                print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")
