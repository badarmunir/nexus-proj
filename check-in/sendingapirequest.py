import requests


def check_user_login():
    response = requests.get("http://192.168.1.242:8081/api/member/checkin/")
    print(response.status_code)
    print(response.json())

    user = "badar.munir@nexuscorp-ltd.com"
    pswd = "system@123"
    parameters = {
        "username": user,
        "password": pswd,
    }
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

    print(response.json())


check_user_login()
