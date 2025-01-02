import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook

# Laden der Daten
df = pd.read_excel("data_history_with_predictions.xlsx")


# Definiere Start- und Enddatum
start_date = "2024-01-01"
end_date = "2024-12-01"

# Konvertiere die "Date"-Spalte in Datetime, falls sie noch nicht im Datetime-Format ist
df["Date"] = pd.to_datetime(df["Date"])

# Filtere den DataFrame nach dem gewünschten Zeitraum
filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

# Erstelle den Plot für den gefilterten Zeitraum
plt.figure(figsize=(10, 6))

# Plot der echten Kurse
plt.plot(filtered_df["Date"], filtered_df["Close"], label="Echte Kurse", color="blue")

# Plot der vorhergesagten Kurse
plt.plot(filtered_df["Date"], filtered_df["Predictions"], label="Vorhergesagter Kurs", color="red", linestyle="--")

plt.xlabel("Datum")
plt.ylabel("Bitcoin Preis in USD")
plt.title(f"Echte vs. Vorhergesagte Kurse vom {start_date} bis {end_date}")

# Legende hinzufügen
plt.legend()

# Anzeige des Plots
plt.xticks(rotation=45)
plt.grid(True)
plt.show()