import requests
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.status_code)
# Filtering the data
params = {"userId": 1}
response = requests.get("https://jsonplaceholder.typicode.com/posts", params = params)
print(response.json())