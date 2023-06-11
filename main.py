import requests
import json

def login(email, password):
    url = "https://discord.com/api/v9/auth/login"
    data = {
        "email": email,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)    
    if response.status_code == 200:
        print("\033[92mLogin successful")
        token = response.json().get("token")
        print("\033[95mToken:\033[0m", token)
    else:
        print("\033[91mLogin failed with status code:\033[0m", response.status_code)

print("\033[95mGet  discord token from credentials\033[0m")
email = input("email: ")
password = input("password: ")

login(email, password)
