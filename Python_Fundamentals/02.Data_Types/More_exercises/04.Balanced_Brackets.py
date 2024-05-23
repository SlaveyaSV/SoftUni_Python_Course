number_of_lines = int(input())

open_bracket = False
is_balanced = True

for _ in range(number_of_lines):
    line = input()

    if line == "(":
        if open_bracket:
            is_balanced = False
            break
        else:
            open_bracket = True
    elif line == ")":
        if open_bracket:
            open_bracket = False
        else:
            is_balanced = False
            break

if is_balanced and not open_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")
