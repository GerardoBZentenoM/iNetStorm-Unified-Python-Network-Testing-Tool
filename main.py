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
**   Release        : 0.0.1
**   Bugs & Fixes   :
**
**   Date           :
**
**
**   Usage          : sudo python3 main.py
   ###########################################################################*/
"""

import os
from art import welcome


print(welcome)

if 'SUDO_UID' not in os.environ.keys():
    print("Try running this program with sudo.")
    print("Try with: 'sudo python3 main.py'")
    exit()
