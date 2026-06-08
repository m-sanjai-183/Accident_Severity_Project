import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Sample dataset
data = {
    'speed': [40, 60, 80, 100, 120],
    'weather': [0, 1, 1, 2, 2],  # 0=Clear,1=Rainy,2=Foggy
    'traffic': [1, 2, 3, 4, 5],
    'severity': [0, 1, 1, 2, 2]  # 0=Low,1=Medium,2=High
}

df = pd.DataFrame(data)

X = df[['speed', 'weather', 'traffic']]
y = df['severity']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open('accident_model.pkl', 'wb'))

print("Model Trained Successfully!")