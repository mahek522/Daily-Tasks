import requests
response = requests.get("https://httpbin.org/user-agent")
print(response.text)