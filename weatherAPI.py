import requests

cityName = input("Enter your city: ")
apiKey = "b789fb4780629eee92013f265a5020e1"

# url="https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
# url="https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={apiKey}"
url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=b789fb4780629eee92013f265a5020e1&units=metric".format(
    cityName)

res = requests.get(url).json()

# print(res["cod"])


if (res["cod"] == 200):
    temp = res["main"]["temp"]
    print("The temp in", cityName, "is", temp, "°C")
else:
    print(res["message"], ": try again")
