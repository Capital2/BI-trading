import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

class PricePredictionAgent:
    def __init__(self, filename, time_step=100):
        self.filename = filename
        self.time_step = time_step
        self.model = self._build_model()
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.data = self._load_data()

    def _load_data(self):
        # Load and preprocess the data
        df = pd.read_csv(self.filename)
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        data = df[['Close']].values
        scaled_data = self.scaler.fit_transform(data)
        return scaled_data

    def _create_dataset(self, dataset):
        X, Y = [], []
        for i in range(len(dataset) - self.time_step - 1):
            a = dataset[i:(i + self.time_step), 0]
            X.append(a)
            Y.append(dataset[i + self.time_step, 0])
        return np.array(X), np.array(Y)

    def _build_model(self):
        # Define and compile the LSTM model
        model = Sequential([
            LSTM(50, return_sequences=True, input_shape=(self.time_step, 1)),
            LSTM(50, return_sequences=False),
            Dense(25),
            Dense(1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def train_model(self, epochs=1, batch_size=1):
        X, y = self._create_dataset(self.data)
        X = X.reshape(X.shape[0], X.shape[1], 1)
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size)

    def predict(self, days):
        # Predict future prices
        predictions = []
        last_data = self.data[-self.time_step:]
        current_batch = last_data.reshape((1, self.time_step, 1))

        for i in range(days):
            current_pred = self.model.predict(current_batch)[0]
            predictions.append(current_pred)
            current_batch = np.append(current_batch[:,1:,:],[[current_pred]],axis=1)

        predicted_prices = self.scaler.inverse_transform(predictions)
        return predicted_prices.flatten()



