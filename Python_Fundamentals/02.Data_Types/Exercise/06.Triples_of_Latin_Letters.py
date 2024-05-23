number_of_letters = int(input())
start_index = ord("a")

for char_1 in range(start_index, start_index+number_of_letters):
    for char_2 in range(start_index, start_index+number_of_letters):
        for char_3 in range(start_index, start_index+number_of_letters):
            print(chr(char_1)+chr(char_2)+chr(char_3))
