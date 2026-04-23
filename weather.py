import requests

API_KEY = "93b53e9147d5c03f089fa8228e86d17f"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()
print(data)
if str(data["cod"]) != "200":
    print("Error:", data)
else:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print(f"\nCity: {city}")
    print(f"Temperature: {temp}°C")
    print(f"Weather: {weather}")
    print(f"Humidity: {humidity}%")