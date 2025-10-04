import tensorflow as tf   
from keras.layers import Dense, Normalization
import keras
from keras.losses import MeanSquaredError
import numpy as np

# Generate training data
x_train = np.array([
    [1.0], [2.0], [3.0], [4.0], [5.0], 
    [6.0], [7.0], [8.0], [9.0], [10.0],
    [11.0], [12.0], [13.0], [14.0], [15.0],
    [16.0], [17.0], [18.0], [19.0], [20.0]
])

y_train = np.array([
    [300.0], [500.0], [700.0], [900.0], [1100.0],
    [1300.0], [1500.0], [1700.0], [1900.0], [2100.0],
    [2300.0], [2500.0], [2700.0], [2900.0], [3100.0],
    [3300.0], [3500.0], [3700.0], [3900.0], [4100.0]
])

# Normalize the data manually for better training
x_mean, x_std = x_train.mean(), x_train.std()
y_mean, y_std = y_train.mean(), y_train.std()

x_train_norm = (x_train - x_mean) / x_std
y_train_norm = (y_train - y_mean) / y_std

# Create model with your original architecture
model = keras.Sequential([
    Dense(units=2, activation="relu", name="layer1"),
    Dense(units=1, activation="linear", name="layer2"),
])

model.compile(
    loss=MeanSquaredError(),
    optimizer=keras.optimizers.Adam(learning_rate=0.01)
)

# Train the model on normalized data
print("Training the model...")
history = model.fit(x=x_train_norm, y=y_train_norm, epochs=1000, verbose=0)

# Make predictions and denormalize
y_pred_norm = model.predict(x_train_norm, verbose=0)
y_pred = y_pred_norm * y_std + y_mean  # Denormalize predictions

# Display results
print("\nSample Predictions vs Actual:")
print("-" * 40)
for i in range(0, len(x_train), 4):  # Show every 4th sample
    print(f"x={x_train[i][0]:5.1f} | Predicted: {y_pred[i][0]:7.2f} | Actual: {y_train[i][0]:7.2f}")

print("\n" + "="*40)
print(f"Final training loss (normalized): {history.history['loss'][-1]:.4f}")

# Calculate mean absolute error on original scale
mae = np.mean(np.abs(y_pred - y_train))
print(f"Mean Absolute Error: {mae:.2f}")

# Test on new data
x_test = np.array([[2.5], [7.5], [15.5]])
x_test_norm = (x_test - x_mean) / x_std
y_test_pred_norm = model.predict(x_test_norm, verbose=0)
y_test_pred = y_test_pred_norm * y_std + y_mean

print("\nPredictions on new data:")
print("-" * 40)
for i in range(len(x_test)):
    expected = 200 * x_test[i][0] + 100  # True relationship
    print(f"x={x_test[i][0]:5.1f} | Predicted: {y_test_pred[i][0]:7.2f} | Expected: {expected:7.2f}")