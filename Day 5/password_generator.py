import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to the project of password generator!")
num_of_letters = int(input("How many letters would you like in your password? \n"))
num_of_symbols = int(input("How many symbols would you like in your password? \n"))
num_of_number = int(input("How many number would you like in your password? \n"))
password = ""

# main code starting from here
#level one
# for char in range(1, num_of_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char
#
# for sym in range(1, num_of_symbols + 1):
#     random_sym = random.choice(symbols)
#     password += random_sym
#
# for num in range(1, num_of_number + 1):
#     random_number = random.choice(numbers)
#     password += random_number



# #level two
# for char in range(0, num_of_letters):
#     password += random.choice(letters)
#
# for sym in range(0, num_of_symbols):
#     password += random.choice(symbols)
#
# for num in range(0, num_of_number):
#     password += random.choice(numbers)
#
#
# print("Final generated password is:", password)

#hard level
password_list = []
for char in range(0, num_of_letters):
    password_list.append(random.choice(letters))

for sym in range(0, num_of_symbols):
    password_list.append(random.choice(symbols))

for num in range(0, num_of_number):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
print("After new version of shuffle generated password is:", password_list)

#now converting password list to string

password_stg = ""

for char in password_list:
    password_stg += char

print("Final generated password is:", password_stg)