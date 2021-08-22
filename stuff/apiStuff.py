import requests

response = requests.get("api.openweathermap.org/data/2.5/weather?q={toronto}&appid={47aa8755b54edbf68ad4e8bd604517a9}")

print(response)