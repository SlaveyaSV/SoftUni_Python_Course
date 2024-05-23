key = int(input())
number_of_letters = int(input())

decrypted_message = ""

for _ in range(number_of_letters):
    letter = input()
    decrypted_message += chr(ord(letter) + key)

print(decrypted_message)
