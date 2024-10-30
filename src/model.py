from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(data):
    X = data[['Max_Temp', 'Min_Temp', 'rainfall', 'Humidity', 'Wind_Speed', 'Cloud_Coverage']]
    y = data['flood_occurred']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model, X_test, y_test