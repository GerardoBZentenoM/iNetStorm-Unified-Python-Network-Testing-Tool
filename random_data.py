import random

from phone_gen import PhoneNumber  # From: https://github.com/tolstislon/phone-gen

# name lists obtain by: https://github.com/terryweiss/ink-collector.git
from sources.first_names import first_names
from sources.last_names import last_names

# Source : https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/500-worst-passwords.txt
from sources.passwords import common_passwords
from sources.email import email_extention, email_domain


def random_name():
    """Generate a random name of the list in /sources/first_names.py and lastnames.py

    Returns:
        str: A complete name with first and lastname
    """
    random_name = random.choice(first_names) + " " + random.choice(last_names)
    return random_name


def random_phone_number(country="USA"):
    """Generate a fake numbre with a country code

    Args:
        country (str, optional): Country code. Defaults to "USA".

    Returns:
        str: a complete random phone number with the according country code
    """
    phone_number = PhoneNumber(country)
    phone_number = phone_number.get_number()
    phone_number = phone_number[1:]
    return phone_number


def random_email(username):
    """Generate a email whit the first and lastname of the person

    Args:
        username (str): Is the name of the person to obtain the email

    Returns:
        str: a complete and valid email
    """
    first_name, last_name = username.split(" ", 1)
    email = f"{first_name}.{last_name}@{random.choice(email_domain)}.{random.choice(email_extention)}"
    return email.lower()


def random__common_password():
    """Select a random password of the most commons

    Returns:
        str: a password in the top of more common
    """
    password = random.choice(common_passwords)
    return password
