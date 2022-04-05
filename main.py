# ! /usr/bin/python
"""
/* #############################################################################
**    File           : main.py
**    Proyect        : DoS-BruteForce-FakeData-Attack
**    IDE            : Visual Studio Code
**    Language       : Python 3.9.7
**    OS             : Ubuntu 21.10
**    Date/Hour      : 03/31/2022
**    Description    :
**         A Python tool to perform DoS, brute force and fake data fill attacks
**         For educational purposes only*
**   Authors         :
**            Gerardo B Zenteno M. https://github.com/GerardoBZentenoM
**
**   Versión        : Beta
**   Revisión       : A
**   Release        : 0.0.2
**   Bugs & Fixes   :
**
**   Date           :
**
**
**   Usage          : sudo python3 main.py
   ###########################################################################*/
"""

import os
import random
import socket

from phone_gen import PhoneNumber  # From: https://github.com/tolstislon/phone-gen
from ipaddress import IPv4Network

from sources.art import welcome
from sources.domain_blacklist import domain_blacklist

# name lists obtain by: https://github.com/terryweiss/ink-collector.git
from sources.first_names import first_names
from sources.last_names import last_names

print(welcome)
print(
    "Description: A Python tool to perform DoS, brute force and fake data fill attacks."
)
print("Please, only use this to educational propose.")
print("DON'T ATTACK LEGITIM WEBSITES. \n")

if "SUDO_UID" not in os.environ.keys():
    print("Try running this program with sudo.")
    print("Try with: 'sudo ./.venv/lib/python3.9/site-packages main.py'")
    exit()


target = input("Enter the IP address to test ej. 192.168.100.80 or test.com \n")
# target = "192.168.100.15"
# target = "google.com"

for domain in domain_blacklist:
    if domain in target:
        print("Please don't use this tool in this website.")
        exit()

try:
    host = target.replace("https://", "").replace("http://", "").replace("www.", "")
    ip_target = socket.gethostbyname(host)
    print(f"ip_target: {ip_target}")
except Exception as e:
    print(e)

net = IPv4Network(ip_target)
print(f"net: {net}")


def random_name():
    try:
        random_name = random.choice(first_names) + " " + random.choice(last_names)
        return random_name
    except Exception as e:
        print(e)


def random_phone_number(country="USA"):
    """This function returns a phone number"""
    phone_number = PhoneNumber(country)
    phone_number = phone_number.get_number()
    phone_number = phone_number[1:]
    return phone_number


# ********************************************************
# In progres


def random_email():
    """Return a random fake armed email (I guess)"""
    # TODO: Make this function
    email = "test@test.com"
    return email


def random_password():
    """This function returns password"""
    # string = ''
    # arr = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#*'
    # for _ in range(n):
    #     string += arr[random.randint(0, 55)]
    # return string
    # pass
    return "supersecurepassword"


# ********************************************************


def post_fake_data(ip_target, username=False, password=False, phone=False, email=False):
    """Attack to post fake data to the target"""
    credentials = {}
    credentials.update({"ip_target": ip_target})
    if username:
        username = random_name()
        credentials.update({"username": username})
    if password:
        password = random_password()
        credentials.update({"password": password})
    if phone:
        phone = random_phone_number()
        credentials.update({"phone": phone})
    if email:
        email = random_email()
        credentials.update({"email": email})
    return credentials


credentials = post_fake_data(net, username=True, password=True, phone=True, email=True)
print(credentials)
