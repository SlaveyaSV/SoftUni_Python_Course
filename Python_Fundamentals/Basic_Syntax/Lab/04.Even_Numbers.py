n = int(input())

for _ in range(n):
    number = int(input())

    if number % 2 != 0:
        print(f"{number} is odd!")
        break

else:
    print("All numbers are even.")

# n = int(input())
#
# all_are_even = True
#
# for _ in range(n):
#     num = int(input())
#     if num % 2 != 0:
#         print(f"{num} is odd!")
#         all_are_even = False
#         break
#
# if all_are_even:
#     print("All numbers are even.")
