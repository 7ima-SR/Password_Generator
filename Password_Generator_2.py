import random
import string
import termcolor
import pyfiglet

digits = string.digits
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
symbols = "!@#$%^&*()-_="

all_characters = list(digits + lower_case + upper_case + symbols)

print(termcolor.colored(pyfiglet.figlet_format("Password Generator"), "red"))
print(termcolor.colored("Powered by Hima", "yellow"))

try:
    password_length = int(input("Enter the length of password: "))

    if password_length < 4:
        print("⚠️ Password should be at least 4 characters (to include all types).")
    else:

        password = [
            random.choice(digits),
            random.choice(lower_case),
            random.choice(upper_case),
            random.choice(symbols)
        ]

        remaining_length = password_length - 4
        password += random.choices(all_characters, k = remaining_length)
        random.shuffle(password)

        print("".join(password))

except ValueError:
    print("⚠️ Please enter a valid number.")
except:
    print("⚠️ Something went wrong.")
