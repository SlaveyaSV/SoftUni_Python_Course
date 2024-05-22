budget = int(input())

info = input()

while info != "End":
    product_price = int(info)
    budget -= product_price

    if budget < 0:
        print("You went in overdraft!")
        break

    info = input()

else:
    print("You bought everything needed.")
