import pandas as pd

def load_flood_data(file_path):
    flood_data = pd.read_csv(file_path)
    flood_data['date'] = pd.to_datetime(flood_data['date'])
    return flood_data