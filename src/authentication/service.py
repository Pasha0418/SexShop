import requests


def activate_user(uid, token):
    url = 'http://127.0.0.1:8000/auth/users/activation/'
    data = {"uid": uid, "token": token}

    response = requests.post(url, data=data)

    if response.status_code == 204:
       return True
    return False


