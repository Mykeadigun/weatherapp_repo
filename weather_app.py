from flask import Flask, request, jsonify
import requests
import datetime

# Create a Flask app
app = Flask(__name__)

@app.route('/')
def home():
    today = datetime.datetime.today()
    return f"Welcome to the Weather App! Today's date is {today:%B %d, %Y}"

@app.route('/weather', methods=['GET'])
def get_weather():
    # Get city and API key from query parameters
    city = request.args.get('city')
    api_key = request.args.get('api_key')

    if not city or not api_key:
        return jsonify({"error": "Please provide both 'city' and 'api_key' as query parameters"}), 400

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

            # Returning weather information as JSON
            return jsonify({
                "city": city_name,
                "temperature": f"{temperature}°C",
                "condition": description.capitalize(),
                "humidity": f"{humidity}%",
                "wind_speed": f"{wind_speed} m/s"
            })
        else:
            return jsonify({"error": f"City not found or error: {data['message']}"}), 404

    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

if __name__ == "__main__":
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000)
