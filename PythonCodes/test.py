import requests
response = requests.get(
    'http://api.aladhan.com/v1/calendarByCity/2017/4?city=Alexandria&country=Egypt&method=5'
)

if response.status_code == 200:
    data = response.json()
    print(data["data"][0]["timings"])