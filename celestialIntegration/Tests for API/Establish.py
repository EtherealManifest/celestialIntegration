import requests, pprint

def confirm_connection():
    CONNECTION_URL = "http://localhost:8090/api"
    try:
        response = requests.get(CONNECTION_URL)
    except requests.exceptions.ConnectionError as e:
        print("Connection Failed! Is Stellarium Running?")
        return 1
    return 0
confirm_connection()