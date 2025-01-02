import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras 
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from keras import Sequential
from keras.layers import Input, Dense, LSTM, Dropout


# Daten einlesen

df = pd.read_excel("data_history_cleaned.xlsx")
print(df.head(5))


# Daten Vorbereitung  

df = df.dropna()
print(df.info())

features = df[["Open","High","Low","Close_before","Changes"]]
target = df["Close"]

feature_scaler = MinMaxScaler()
target_scaler = MinMaxScaler()

features = feature_scaler.fit_transform(features)
target = target_scaler.fit_transform(target.values.reshape(-1, 1))

# Tages-Sequenzen

def create_sequence(features, target, length):

    X = []
    y = []

    for i in range(len(features) - length):
        X.append(features[i:i+length])
        y.append(target[i+length])
    return np.array(X), np.array(y)

length = 20
X, y = create_sequence(features, target,length)

print(X)
print(X.shape)
print(y.shape)

# Modell erstellen

model = Sequential()
model.add(Input(shape=(20, 5)))
model.add(LSTM(32, return_sequences = True))
model.add(Dropout(0.2))
model.add(LSTM(16))
model.add(Dropout(0.2))
model.add(Dense(1))

model.compile(optimizer="adam",loss="mse")

# Daten aufteilen

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state = 42)

# Modell trainieren

history = model.fit(X_train, y_train, epochs= 50, batch_size= 32)
print(model.summary())

# Genauigkeit

evaluation = model.evaluate(X_test, y_test)
evaluation_train = model.evaluate(X_train, y_train)

print(f"Genauigkeit Test: {evaluation * 100}")
print(f"Genauigkeit Train: {evaluation_train * 100}")

# Predictions in die Tabelle einfügen

predictions = model.predict(X_test)
print(model.evaluate(X_test, y_test))

predictions_rescaled = target_scaler.inverse_transform(predictions.reshape(-1, 1))
print(predictions)
print(X.shape)



predictions_rescaled = predictions_rescaled.reshape(-1)


#df["Predictions"] = np.nan  
#df.iloc[length:, df.columns.get_loc("Predictions")] = predictions_rescaled 

#df = df.dropna(subset=["Predictions"])

#df.to_excel("data_history_with_predictions.xlsx", index=False)




# Modell speichern

#model.save("model.h5")
#model.save("model.keras")


y_test_rescaled = target_scaler.inverse_transform(y_test.reshape(-1, 1))

# Zeitraum definieren
start_index = 0  
end_index = 75  


y_test_subset = y_test_rescaled[start_index:end_index]
predictions_subset = predictions_rescaled[start_index:end_index]

# Plot erstellen

plt.figure(figsize=(10, 6))


plt.plot(y_test_subset, label="Echte Werte (Testdaten)", color="blue", marker="o", linestyle="-", markersize=4)


plt.plot(predictions_subset, label="Vorhersagen", color="red", marker="x", linestyle="--", markersize=4)


plt.xlabel("Index (kleiner Zeitraum)")
plt.ylabel("Bitcoin Preis in USD")
plt.title(f"Echte Werte vs. Vorhersagen (Zeitraum: {start_index} bis {end_index})")
plt.legend()
plt.grid(True)

#plt.savefig("bitcoin_prognose.png")

# Plot anzeigen


plt.show()




