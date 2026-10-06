from random import *
from string import *

def generate_password(flag_lower, flag_upper, flag_special, flag_digits, length):
    alf = ""
    password = ""
    if flag_lower:
        alf += ascii_lowercase
        password += choice(ascii_lowercase)

    if flag_upper:
        alf += ascii_uppercase
        password += choice(ascii_uppercase)

    if flag_special:
        alf += punctuation
        password += choice(punctuation)

    if flag_digits:
        alf += digits
        password += choice(digits)

    if not alf:
        return "Нужно выбрать хотя бы один фильтр"

    if length < len(password):
        return "Недопустимая длина с учетом выбраных фильтров"

    while len(password) < length:
        password += choice(alf)

    password = list(password)
    shuffle(password)
    return ''.join(password)

print("=" * 35)
print("       ГЕНЕРАТОР ПАРОЛЕЙ")
print("=" * 35)

length = int(input("\nВведите длину пароля: "))
flag_lower = input("Нужно использовать строчные буквы? (да/нет): ").lower() == "да"
flag_upper = input("Нужно использовать заглавные буквы? (да/нет): ").lower() == "да"
flag_special = input("Нужно использовать специальные символы? (да/нет): ").lower() == "да"
flag_digits = input("Нужно использовать цифры? (да/нет): ").lower() == "да"

print("\n" + "-" * 35)
print("Ваш пароль:", generate_password(flag_lower, flag_upper, flag_special, flag_digits, length))
print("-" * 35)