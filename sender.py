import requests

response = requests.post(
    'http://127.0.0.1:5000/send',
    json={"username": "Nick", "text": "Hello all!!!"}
)
print(response.status_code)
print(response.text)
print(response.json())
