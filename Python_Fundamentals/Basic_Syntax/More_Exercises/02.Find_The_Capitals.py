string = input()
capital_letters = []

for i in range(len(string)):
    if string[i].isupper():
        capital_letters.append(i)

print(capital_letters)

