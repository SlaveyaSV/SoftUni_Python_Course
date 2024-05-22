n = int(input())

for row in range(1, n+1):
    print("*" * row)
for row in range(n-1, 0, -1):
    print("*" * row)

# Another solution:
#
# n = int(input())
#
# for row in range(1, n+1):
#     for column in range(0, row):
#         print("*", end="")
#
#     print()
#
# for row in reversed(range(1, n)):
#     for column in range(0, row):
#         print("*", end="")
#
#     print()
