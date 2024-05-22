number_of_coffees = 0

while True:
    command = input()

    if command == "END":
        break

    if (command.lower() == "coding" or
            command.lower() == "dog" or
            command.lower() == "cat" or
            command.lower() == "movie"):
        if command.islower():
            number_of_coffees += 1
        else:
            number_of_coffees += 2

if number_of_coffees > 5:
    print("You need extra sleep")
else:
    print(number_of_coffees)

