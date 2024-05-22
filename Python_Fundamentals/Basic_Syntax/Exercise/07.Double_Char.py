while True:
    string = input()

    if string == "End":
        break

    if string != "SoftUni":
        new_string = ""
        for char in string:
            new_string += char * 2
        print(new_string)
