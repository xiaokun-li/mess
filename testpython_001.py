import requests
import pandas as pd
import matplotlib.pyplot as plt

# Assuming the OpenWeatherMap API Key and the city name are given
API_KEY = 'YOUR_API_KEY_HERE'
CITY_NAME = 'YOUR_CITY_NAME_HERE'

# Function to fetch weather data
def fetch_weather_data(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    return response.json()

# Function to transform data into a pandas DataFrame
def transform_data_to_dataframe(weather_data):
    # Extract the list of forecasts
    forecast_list = weather_data['list']
    # Prepare data for DataFrame
    data = {
        'datetime': [forecast['dt_txt'] for forecast in forecast_list],
        'temperature': [forecast['main']['temp'] for forecast in forecast_list]
    }
    df = pd.DataFrame(data)
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

# Function for basic data analysis
def analyze_data(df):
    mean_temp = df['temperature'].mean()
    median_temp = df['temperature'].median()
    temp_range = df['temperature'].max() - df['temperature'].min()
    return mean_temp, median_temp, temp_range

# Function for data visualization
def visualize_data(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['datetime'], df['temperature'], marker='o', linestyle='-', color='b')
    plt.title('Temperature Trend for the Next 24 Hours')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to orchestrate the fetching, transformation, analysis, and visualization
def main(api_key, city_name):
    weather_data = fetch_weather_data(api_key, city_name)
    df = transform_data_to_dataframe(weather_data)
    mean_temp, median_temp, temp_range = analyze_data(df)
    print(f"Mean Temperature: {mean_temp:.2f}°C")
    print(f"Median Temperature: {median_temp:.2f}°C")
    print(f"Temperature Range: {temp_range:.2f}°C")
    visualize_data(df)

# Assuming the API key and city name are correctly set
# Uncomment the following line to run the script with your own API key and city name
# main(API_KEY, CITY_NAME)

# NOTE: Please replace 'YOUR_API_KEY_HERE' and 'YOUR_CITY_NAME_HERE' with your actual API key and city name before running the script.
