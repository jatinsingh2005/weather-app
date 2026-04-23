import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter city name: ").strip().title()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()
except:
    print("Network error ❌")
    exit()

if str(data["cod"]) != "200":
    print("Invalid city or API issue ❌")
else:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print("\n🌍 City:", city)
    print("🌡 Temperature:", temp, "°C")
    print("🌥 Weather:", weather)
    print("💧 Humidity:", humidity, "%")
