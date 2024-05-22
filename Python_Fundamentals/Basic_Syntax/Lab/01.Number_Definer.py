num = float(input())

size = ""
if abs(num) < 1:
    size = "small "
elif abs(num) > 1000000:
    size = "large "

if num == 0:
    print("zero")
elif num > 0:
    print(f"{size}positive")
elif num < 0:
    print(f"{size}negative")


# number = float(input())
#
# if number == 0:
#     print("zero")
# elif number > 0:
#     if number < 1:
#         print("small positive")
#     elif number > 1000000:
#         print("large positive")
#     else:
#         print("positive")
# elif number < 0:
#     if number > -1:
#         print("small negative")
#     elif number < -1000000:
#         print("large negative")
#     else:
#         print("negative")
