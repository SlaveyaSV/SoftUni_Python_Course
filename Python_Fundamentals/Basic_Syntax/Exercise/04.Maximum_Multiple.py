divisor = int(input())
boundary = int(input())

# reversed - the first found will be the greatest:
for num in range(boundary, 0, -1):
    if num % divisor == 0:
        print(num)
        break

