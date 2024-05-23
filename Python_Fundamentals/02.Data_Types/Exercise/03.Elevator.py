from math import ceil

number_of_people = int(input())
elevator_capacity = int(input())

courses_count = ceil(number_of_people / elevator_capacity)

print(courses_count)

# Another solution:
#
# number_of_people = int(input())
# elevator_capacity = int(input())
#
# if number_of_people % elevator_capacity == 0:
#     courses_count = number_of_people // elevator_capacity
# else:
#     courses_count = number_of_people // elevator_capacity + 1
#
# print(courses_count)
