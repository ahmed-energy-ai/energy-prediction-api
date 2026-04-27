import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

np.random.seed(42)

# Create data
hours = pd.date_range(start="2023-01-01", periods=1000, freq="h")

data = pd.DataFrame({
    "timestamp": hours
})

data["temperature"] = np.random.uniform(15, 40, size=len(data))

# Features
data["hour"] = data["timestamp"].dt.hour
data["hour_sin"] = np.sin(2 * np.pi * data["hour"] / 24)
data["hour_cos"] = np.cos(2 * np.pi * data["hour"] / 24)

# Target
data["kWh"] = (
    50
    + data["temperature"] * 1.5
    + (data["temperature"] ** 2) * 0.02
    + np.sin(data["hour_sin"] * 3) * 10
    + np.random.normal(0, 3, size=len(data))
)

X = data[["temperature", "hour_sin", "hour_cos"]]
y = data["kWh"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Model
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

preds = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, preds))
import joblib
joblib.dump(model, "model.pkl")

# Save model
joblib.dump(model, "model.pkl")