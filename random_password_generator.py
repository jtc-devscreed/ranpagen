import random
import string

print('Hi, Welcome to Random Password Generator!')

while True:
    try:
        # Note: Python 2.x users should user raw_input, the equivalent of
        length = int(input('\nPlease enter your desired length for your password: '))
    except ValueError:
        print("Sorry, please enter a valid number.")
        # better try again... Return to the start of the loop
        continue
    else:
        # length was successfully parsed!
        # we are ready to exit the loop.
        break

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, length)
password = "".join(temp)
if length <= 94:
    print(password)
else:
    print("Please enter a number not greater than 94.")