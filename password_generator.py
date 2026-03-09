import random
import string

print("Password Generator ")

length = int(input("Enter password length: "))

# символи для пароля
characters = string.ascii_letters + string.digits + "!@#$%&?.,"

# створення випадкового пароля
password = "".join(random.choice(characters) for _ in range(length))

print(f"Your password: {password}")