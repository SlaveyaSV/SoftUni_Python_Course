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

# budget = int(input())
#
# while True:
#     command = input()
#
#     if command == "End":
#         print("You bought everything needed.")
#         break
#     else:
#         price = int(command)
#
#     if price <= budget:
#         budget -= price
#     else:
#         print("You went in overdraft!")
#         break
