import requests
response = requests.get("https://httpbin.org/status/404")
if response.status_code == requests.codes.not_found:
    print("The page was not found.")
else:
    print(response.status_code)