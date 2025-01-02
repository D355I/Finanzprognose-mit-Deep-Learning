import pandas as pd
import numpy as np

# Daten einlesen
df = pd.read_excel("data_history_raw.xlsx")

if not df.empty:
    print("Data eingelesen!")
    print(df.head(10))
else:
    print("Data nicht eingelesen!")


# Informationen anzeigen

print(df.dtypes)
print(df.info())

# Spalten vorverarbeiten:
# Der Close-Wert jedes Tages wird genommen und verschoben (Close). Anschließend wird berechnet wie viel der Wert des nächsten Tages (Close) mit dem des letzten
# Tages (Close_before) abweicht (Changes)

print(df["Close"])
df["Close"] = df["Close"].shift(1)
print(df.head(10))
df["Close_before"] = df["Close"].shift(-1)
print(df.head(10))
df["Changes"] = (df["Close"] / df["Close_before"]) -1 
print(df.head(10))

df = df.dropna()
df.to_excel("data_history_cleaned.xlsx", index=False)


