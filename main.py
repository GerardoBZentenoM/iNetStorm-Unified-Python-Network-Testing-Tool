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
import socket
from ipaddress import IPv4Network

from art import welcome
from domain_blacklist import domain_blacklist

print(welcome)

if "SUDO_UID" not in os.environ.keys():
    print("Try running this program with sudo.")
    print("Try with: 'sudo python3 main.py'")
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
