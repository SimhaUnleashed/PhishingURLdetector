import requests

base = "http://127.0.0.1:5000/"

#response = requests.get(base+ "adult/Oni Chichi: Re-born")
response = requests.get(base+ "https://www.facelook.com")
print(response.json())