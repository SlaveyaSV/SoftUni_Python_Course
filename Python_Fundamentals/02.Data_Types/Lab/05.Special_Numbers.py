n = int(input())

for num in range(1, n+1):
    digits_sum = 0

    for digit in range(len(str(num))):
        digits_sum += int(str(num)[digit])

    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
