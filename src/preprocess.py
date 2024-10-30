import pandas as pd

def preprocess_data(api_data, flood_data):
    api_df = pd.DataFrame([api_data])  # Convert API data to DataFrame
    api_df['date'] = pd.to_datetime(api_df['dt'], unit='s')  # Convert timestamp to datetime

    # Merging datasets on date
    flood_data['date'] = pd.to_datetime(flood_data['Year'].astype(str) + '-' + flood_data['Month'].astype(str) + '-01')
    combined_data = pd.merge(api_df, flood_data, on='date', how='outer')

    # Filling NaN values
    combined_data['rainfall'] = combined_data['rainfall'].fillna(0)
    combined_data['flood_occurred'] = combined_data['flood?'].apply(lambda x: 1 if x == 1 else 0)
    
    return combined_data