import requests
import datetime

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")


def get_weather(city, api_key):
    try:
        # API endpoint
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        # Sending a GET request
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extracting weather details
            city_name = data['name']
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Displaying the weather information
            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Condition: {description.capitalize()}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"City not found or error: {data['message']}")


    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    print("Welcome to the Weather App!")
    print(f"{today:%B %d, %Y}")
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter the name of the city: ")
    get_weather(city, api_key)