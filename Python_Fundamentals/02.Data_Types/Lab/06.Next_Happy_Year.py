year = int(input()) + 1

while len(str(year)) != len(set(str(year))):
    year += 1

print(year)
