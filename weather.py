import requests
api="441383f74d7e45c0a2e170615230611"
user=input("Enter City: ")
weather=requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user}&appid={api}")
print(weather.status_code)
