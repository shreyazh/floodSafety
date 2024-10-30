# Flood Prediction Application

## Overview

This application predicts the probability of flooding based on weather data. Users can input their name and the city for which they want to check flood predictions. The application fetches weather data from the OpenWeather API and uses a machine learning model to make predictions.

## Features

- User input for name and city.
- Fetches current weather data.
- Predicts flood probability based on weather conditions.
- Personalized greeting for users.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/floodSafety.git
   cd floodSafety
   
2.Install Required Packages: Make sure you have Python and pip installed. Then, install the required packages:
pip install -r requirements.txt

3. Update API Key: Open src/setup.py and replace YOUR_API_KEY_HERE with your actual OpenWeather API key.

4. Run the Application: Start the Streamlit application:
   streamlit run src/app.py

5. Access the Application: Open your web browser and navigate to http://localhost:8501.

## Code Changes

1. Renamed Fetcher File
The fetcher file has been renamed from fetch_weather.py to setup.py. Update your imports accordingly.

2. User Input for Name
The application now includes an input field for the user's name. The updated code in src/app.py includes:
# User input for name
user_name = st.text_input("Enter Your Name:")

3. Error Handling for Weather Data Fetching
To improve user experience, error handling has been added to manage cases where weather data cannot be fetched. The following error message is displayed if the city name is incorrect or if there are issues with the API:
if "error" in weather_data:
    st.error(weather_data["error"])

Troubleshooting Weather Data Fetching
If you encounter the error "Could not fetch weather data. Please check the city name," consider the following:

*Incorrect City Name*: Ensure the city name is spelled correctly and formatted properly (e.g., "San Francisco").
*Geocoding API*: Use the OpenWeather Geocoding API to verify city names.
*City Availability*: Check if the city is supported by OpenWeather.
*API Key Issues*: Ensure your API key is valid and included in the request.
*Subscription Limitations*: Verify that you are not exceeding request limits for your API plan.
*Error Handling in Code*: Implement error handling to capture specific error messages from the API.

## Conclusion
This flood prediction application provides a simple interface for users to check flood probabilities based on current weather data. By following the setup instructions and troubleshooting tips, you can successfully run the application and make use of its features.


### Notes

- Replace `https://github.com/yourusername/floodSafety.git` with the actual URL of your GitHub repository.
- Ensure that the file names and paths in the instructions match your project structure.
- You can add more sections or details as needed to fit your project's requirements.
