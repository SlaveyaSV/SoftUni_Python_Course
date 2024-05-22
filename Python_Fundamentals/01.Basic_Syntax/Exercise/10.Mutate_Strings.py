first_string = input()
second_string = input()

for char in range(len(first_string)):
    transformed_string = second_string[:char+1] + first_string[char+1:]
    if transformed_string != first_string:
        first_string = transformed_string
        print(first_string)


# Solution with Replace and String Slices:
#
# s1 = input()
# s2 = input()
#
# for i in range(len(s1)):
#    if s1[i] != s2[i]:
#        s1 = s1[:i] + s1[i:i + 1].replace(s1[i], s2[i], 1) + s1[i + 1:]
#        print(s1)



