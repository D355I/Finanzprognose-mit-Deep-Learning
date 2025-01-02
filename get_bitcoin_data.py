import yfinance as yf
import pandas as pd

data = yf.Ticker("BTC-USD")
hist_data = data.history(period="max")

#Das formatieren zu Excel bringt ein Problem mit der Zeitzonenformatierung mit sich.
#Diese wird umgangen, indem die Zeitzone hier entfernt wird und dann in Excel die Zelle umgewandelt wird!

hist_data.index = hist_data.index.tz_localize(None)

df = pd.DataFrame(hist_data)

 
df.to_excel("data_history_raw.xlsx")

