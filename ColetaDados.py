import yfinance as yf
import pandas as pd

# Definição do ativo e período de análise
symbol = "DIS"
start_date = "2018-01-01"
end_date = "2024-07-20"

# Download dos dados históricos
df = yf.download(
    tickers=symbol,
    start=start_date,
    end=end_date,
    interval="1d",
    progress=False
)

# Seleção do preço de fechamento
df = df[["Close"]]

# Remoção de valores ausentes
df.dropna(inplace=True)
