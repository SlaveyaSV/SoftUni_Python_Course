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
