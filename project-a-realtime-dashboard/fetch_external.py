import requests
import json


def my_function():
    x = requests.get("https://catfact.ninja/facts")
    data = json.loads(x.text)
    print("Status Code", x.status_code)
    for y in data["data"][:3]:
        print(y)


my_function()
