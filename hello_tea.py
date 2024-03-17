import requests

def hello_tea_func():
    response = requests.get('https://app.tea.xyz/')
    print("Hello teaxyzzz4!")
    print("Status teaxyzzz4:", response.url, response.ok)
