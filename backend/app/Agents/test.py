import pandas as pd
import numpy as np

df = pd.read_csv('btc.csv')
df.dropna(inplace=True)
df.to_csv('data_btc.csv')


