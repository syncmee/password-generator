import random

#sync-password-generator
print("Welcome to Password Generator")
number_of_letters = int(input("How many letters you want in your password?\n"))
number_of_symbols = int(input("How many symbols you want in your password?\n"))
number_of_numbers = int(input("How many numbers you want in your password?\n"))

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

for char in range(1, number_of_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, number_of_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, number_of_numbers + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
