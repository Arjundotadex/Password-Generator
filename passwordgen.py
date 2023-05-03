import random

print("Welcome to your Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*1234567890"

number = input("How many passwords you want to generate?:")
number = int(number)

length = int(input("What will be the length of your password?: "))
length = int(length)

print("\n Here are you passwords as requested: ")

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
