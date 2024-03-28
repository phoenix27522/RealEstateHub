#!/usr/bin/python3
import requests

url = "http://0.0.0.0:5000/API/v1/status"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("API endpoint is accessible. Response:")
    print(data)
else:
    print("Error: Failed to access API endpoint. Status code:", response.status_code)
