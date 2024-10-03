import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
import pickle

# Load the dataset
data = pd.read_csv('Timeseries_dataset.csv')

# Convert the 'Timestamp' column to a datetime format and set it as the index
data['Timestamp'] = pd.to_datetime(data['Timestamp'], unit='D', origin='1899-12-30')
data.set_index('Timestamp', inplace=True)

# Check for NaN values in the dataset
print(data.isna().sum())

# Fill NaN values if necessary (you can also drop them if needed)
data.fillna(method='ffill', inplace=True)  # Forward fill to handle NaNs

# Extract the 'Label' column and normalize it
values = data['Label'].values.reshape(-1, 1)

# Check for any infinite values and replace them if necessary
values[~np.isfinite(values)] = 0  # Replace infinite values with 0

# Scale the data to the range (0, 1)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_values = scaler.fit_transform(values)

# Save the scaler for later use during predictions
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

# Function to create sequences for LSTM
def create_sequences(data, time_steps=10):
    sequences, labels = [], []
    for i in range(len(data) - time_steps):
        sequences.append(data[i:i + time_steps])
        labels.append(data[i + time_steps])
    return np.array(sequences), np.array(labels)

# Create sequences
time_steps = 1
X, y = create_sequences(scaled_values, time_steps)

# Split the data into training and testing sets (80% training, 20% testing)
split_index = int(len(X) * 0.8)
X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

# Build the LSTM model
model = Sequential([
    LSTM(150, activation='relu', kernel_initializer='glorot_uniform', input_shape=(time_steps, 1)),
    Dense(1)  # Output a single value for regression
])

# Compile the model with a lower learning rate and gradient clipping
optimizer = Adam(learning_rate=0.001, clipvalue=1.0)  # Gradient clipping to avoid exploding gradients
model.compile(optimizer=optimizer, loss='mean_squared_error')

# Train the model with a smaller batch size and monitor NaN issues
history = model.fit(X_train, y_train, epochs=10, batch_size=64, validation_data=(X_test, y_test))

# Check for NaN values in predictions during training
predictions = model.predict(X_train)
print(f"Number of NaN values in predictions: {np.isnan(predictions).sum()}")  # Should return 0

# Save the trained model
model.save('timeseries_lstm_model.h5')

loss = model.evaluate(X_test, y_test)
print(f"Test loss: {loss}")
