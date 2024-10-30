import streamlit as st
from setup import fetch_weather_data
from load_flood_data import load_flood_data
from preprocess import preprocess_data
from model import train_model
from evaluate_model import evaluate_model

def main():
    st.title("Flood Probability Prediction")

    # User input for name
    user_name = st.text_input("Enter Your Name:")

    # User input for city
    city = st.text_input("Enter City Name:")

    if st.button("Predict Flood Probability"):
        if not user_name:
            st.warning("Please enter your name.")
            return
        
        if not city:
            st.warning("Please enter a city name.")
            return

        # ffetching weather data
        weather_data = fetch_weather_data(city)
        
        if "error" in weather_data:
            st.error(weather_data["error"])
        else:
            flood_data = load_flood_data('data/FloodPrediction.csv')  # Loadin historical data
            
            # Preprocessig data
            combined_data = preprocess_data(weather_data, flood_data)
            
            # Training model
            model, X_test, y_test = train_model(combined_data)
            
            # evaluating model
            accuracy = evaluate_model(model, X_test, y_test)
            st.write(f'Model Accuracy: {accuracy:.2f}')
            
            # displaying predictions
            input_data = [[combined_data['Max_Temp'].iloc[-1], combined_data['Min_Temp'].iloc[-1], combined_data['rainfall'].iloc[-1], 
                           combined_data['Humidity'].iloc[-1], combined_data['Wind_Speed'].iloc[-1], combined_data['Cloud_Coverage'].iloc[-1]]]
            prediction = model.predict(input_data)
            st.write(f"Hello, {user_name}! Based on the current weather data,")
            st.write('Flood predicted' if prediction[0] == 1 else 'No flood predicted')

if __name__ == "__main__":
    main()