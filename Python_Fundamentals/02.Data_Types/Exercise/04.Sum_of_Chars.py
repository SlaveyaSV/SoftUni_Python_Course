number_of_chars = int(input())

ascii_sum = 0

for _ in range(number_of_chars):
    char = input()
    ascii_sum += ord(char)

print(f"The sum equals: {ascii_sum}")
