from random_data import (
    random__common_password,
    random_email,
    random_name,
    random_phone_number,
)


def post_fake_data(ip_target, username=False, password=False, phone=False, email=False):
    """Attack to post fake data to the target"""
    credentials = {}
    credentials.update({"ip_target": ip_target})
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
    return credentials
