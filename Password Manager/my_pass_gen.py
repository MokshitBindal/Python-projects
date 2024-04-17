
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input("How many symbols would you like?\n"))
# nr_numbers = int(input("How many numbers would you like?\n"))


nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

def generate_pass():
    passlist = []

    pass_letters = [random.choice(letters) for i in range(nr_letters)]
    # print(pass_letters)

    pass_symbols = [random.choice(numbers) for i in range(nr_symbols)]
    # print(pass_symbols)

    pass_numbers = [random.choice(symbols) for i in range(nr_numbers)]
    # print(pass_numbers)

    passlist = pass_letters + pass_symbols + pass_numbers

    random.shuffle(passlist)

    password = "".join(passlist)
    # password = ""
    # for p in passlist:
    #     password += p

    return password
print(generate_pass())



# easy level : a random password,not completely, position of letters and numbers can be same
'''
password = ""

for i in range(nr_letters):
    pass_letters = random.choice(letters)
    password += pass_letters

for i in range(nr_symbols):
    pass_symbols = random.choice(symbols)
    password += pass_symbols

for i in range(nr_numbers):
    pass_numbers = random.choice(numbers)
    password += pass_numbers

'''

# hard level : complete random password
'''
passlist = []
total = nr_symbols + nr_numbers + nr_letters
for i in range(nr_letters):
    pass_letters = random.choice(letters)
    passlist.append(pass_letters)

for i in range(nr_symbols):
    pass_symbols = random.choice(symbols)
    passlist.append(pass_symbols)

for i in range(nr_numbers):
    pass_numbers = random.choice(numbers)
  #  passlist += pass_numbers
    passlist.append(pass_numbers)

random.shuffle(passlist)
password = ""
for p in passlist:
    password += p

print(password)'''



# Another way
'''
access = 0
j = 0
k = 0
l = 0
password = ""
total = nr_symbols + nr_numbers + nr_letters
while len(password) != total:
    choice = random.randint(1,3)

    if choice == 1:
        access = nr_letters
        if access != j:
            pass_letters = random.choice(letters)
            password += pass_letters
            j += 1
            
    elif choice == 2:
        access = nr_symbols
        if access != k:
            pass_symbols = random.choice(symbols)
            password += pass_symbols
            k += 1

    elif choice == 3:
        access = nr_numbers
        if access != l:
            pass_numbers = random.choice(numbers)
            password += pass_numbers
            l += 1
print(password)
'''
