"""
This is an password generator app
"""
import random
import string
import argparse


def generate_password() -> str:
    """
    Generates a random password
    """
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    length = random.randint(8, 20)
    password_list = [''] * length
    for i in range(length):
        char_choice = random.randint(1, 4)
        if char_choice == 1:
            password_list[i] = random.choice(lower_case)
        if char_choice == 2:
            password_list[i] = random.choice(upper_case)
        if char_choice == 3:
            password_list[i] = random.choice(digits)
        if char_choice == 4:
            password_list[i] = random.choice(special)

    return "".join(password_list)


def has_any(line: str, chars: str) -> bool:
    """
    Returns True if some of chars is present in line. Else False
    """
    for char in chars:
        if char in line:
            return True

    return False


def is_password_save(password: str) -> tuple[bool, str]:
    """
    Returns True, "" if password is safe, else False and messages with its problems
    """
    has_lower = has_any(password, string.ascii_lowercase)
    has_upper = has_any(password, string.ascii_uppercase)
    has_digits = has_any(password, string.digits)
    has_special = has_any(password, string.punctuation)
    long_enough = len(password) >= 8

    message = []
    if not has_lower:
        message.append("The password must contain lower case characters")
    if not has_upper:
        message.append("The password must contain upper case characters")
    if not has_digits:
        message.append("The password must contain digits")
    if not has_special:
        message.append("The password must contain special characters")
    if not long_enough:
        message.append("The passord must be at least 8 characters long")

    is_safe = has_lower and has_upper and has_digits and has_special and long_enough

    return is_safe, message


def generate_safe_password() -> str:
    """
    Generates a random password until it's safe
    """
    password = ""
    while not is_password_save(password)[0]:
        password = generate_password()

    return password


def parse_args():
    """
    Parses cmd argument
    """
    parser = argparse.ArgumentParser("The program to generate and check passwords")
    parser.add_argument("--gen", action="store_true")
    parser.add_argument("--check", type=str)

    return parser.parse_args()


def main():
    """
    main function
    """
    args = parse_args()
    if args.gen:
        print(generate_safe_password())
    elif args.check:
        is_safe, problems = is_password_save(args.check)
        if is_safe:
            print("Your password is safe")
        else:
            print("The problems:")
            print("", *problems, sep="\n\t")
    else:
        print("Nothing to do...")


if __name__ == "__main__":
    main()
