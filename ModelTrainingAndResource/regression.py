import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import pickle

# Load the dataset
data = pd.read_csv('Regression_dataset.csv', low_memory=False)

# Data preprocessing
data['V14'] = pd.to_numeric(data['V14'], errors='coerce')
data['V16'] = pd.to_numeric(data['V16'], errors='coerce')

# Fill missing values with 0
data = data.fillna(0)

# Apply log transformation to the target variable 'Label'
data['Label'] = data['Label'].apply(lambda x: np.log1p(x))

# List of skewed features to apply log transformation to
skewed_features = ['V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28']
for feature in skewed_features:
    data[feature] = data[feature].apply(lambda x: np.log1p(x))

# Separate features (X) and the target variable (y)
X = data.drop(columns=['Label'])
y = data['Label']

# Split data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features using MinMaxScaler
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# XGBoost Regressor Model
model = xgb.XGBRegressor(
    objective='reg:squarederror',  # Squared error loss function
    n_estimators=500,              # Number of trees
    learning_rate=0.01,            # Learning rate
    max_depth=6,                   # Max depth of trees
    subsample=0.8,                 # Subsample ratio of the training instances
    colsample_bytree=0.8           # Subsample ratio of columns when constructing each tree
)

# Train the model on the scaled data
model.fit(X_train_scaled, y_train)

# Convert the trained model to a Booster object (used for saving as JSON)
booster_model = model.get_booster()

# Make predictions on the test set
predictions = model.predict(X_test_scaled)

# Calculate and print the Mean Squared Error (MSE) for evaluation
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

# Save the trained model directly in the current directory as JSON
booster_model.save_model('xgboost_regression_model.json')

# Save the scaler in the current directory
with open('xboost_scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)