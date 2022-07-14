import random

from phone_gen import PhoneNumber  # From: https://github.com/tolstislon/phone-gen

# name lists obtain by: https://github.com/terryweiss/ink-collector.git
from sources.first_names import first_names
from sources.last_names import last_names

# Source : https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/500-worst-passwords.txt
from sources.passwords import common_passwords
from sources.email import email_extention, email_domain


def random_name():
    """Returns a random name of the list in first_names.py and last_name.py"""
    random_name = random.choice(first_names) + " " + random.choice(last_names)
    return random_name


def random_phone_number(country="USA"):
    """Returns a phone number"""
    phone_number = PhoneNumber(country)
    phone_number = phone_number.get_number()
    phone_number = phone_number[1:]
    return phone_number


def random_email(username):
    """Return a random fake armed email"""
    first_name, last_name = username.split(" ", 1)
    email = f"{first_name}.{last_name}@{random.choice(email_domain)}.{random.choice(email_extention)}"
    return email.lower()


def random__common_password():
    """This function returns a password from the common list in file passwords.py"""
    password = random.choice(common_passwords)
    return password
