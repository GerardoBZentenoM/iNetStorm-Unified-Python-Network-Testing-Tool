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

from attacks import post_fake_data

from sources.art import welcome
from validations import target_validation


print(welcome)
print(
    "Description: A Python tool to perform DoS, brute force and fake data fill attacks."
)
print("Please, only use this to educational propose.")
print("DON'T USE IN LEGITIM WEBSITES.\n")

# if "SUDO_UID" not in os.environ.keys():
#     print("Try running this program with sudo.")
#     print("Try with: 'sudo ./.venv/lib/python3.9/site-packages main.py'")
#     exit()


target = input("Enter the IP address to test ej. 192.168.100.80 or test.com \n")
target_ip = target_validation(target)

print(f"The direcction of the target is: {target_ip}")

attack = input(
    """
Select some of the folowing tests:
1) Post random and fake data
2) DoS Attack
3)Ping of the death test

: """
)

if attack == "1":
    print("Post in the target the following data: ")
    credentials = post_fake_data(
        target_ip, username=True, password=True, phone=True, email=True
    )
    print(credentials)
elif attack == "2":
    print("DoS Attack")
else:
    print("Another attack")
