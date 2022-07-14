import socket
from ipaddress import IPv4Network
from sources.domain_blacklist import domain_blacklist


def target_validation(target):
    for domain in domain_blacklist:
        if domain in target:
            print("Please don't use this tool in this website.")
            exit()
    try:
        host = target.replace("https://", "").replace("http://", "").replace("www.", "")
        ip_target = socket.gethostbyname(host)
        print(f"ip_target: {ip_target}")
        target_ip = IPv4Network(ip_target)
        print(f"net: {target_ip}")
        return target_ip
    except Exception as e:
        print(e)
        print(
            "******************************************************************************"
        )
        print(
            "ERROR: Sorry, I was unable to get the address of the target, try with another"
        )
        print(
            "******************************************************************************"
        )
        exit()
