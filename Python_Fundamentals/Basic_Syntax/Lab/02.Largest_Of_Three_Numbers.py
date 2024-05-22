from sys import maxsize

max_num = -maxsize

for _ in range(3):
    num = int(input())
    if num > max_num:
        max_num = num

print(max_num)


# first_num = int(input())
# second_num = int(input())
# third_num = int(input())
#
# if first_num > second_num and first_num > third_num:
#     print(first_num)
# elif second_num > first_num and second_num > third_num:
#     print(second_num)
# else:
#     print(third_num)
