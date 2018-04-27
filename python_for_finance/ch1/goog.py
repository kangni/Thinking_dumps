import numpy as np
import pandas as pd
import pandas_datareader.data as web

goog = web.DataReader(
    'GOOG',
    data_source='morningstar',
    start='3/14/2009',
    end='4/14/2018')

goog.tail()

goog['Log_Ret'] = np.log(goog['Close'] / goog['Close'].shift(1))

goog['Volatility'] = pd.Series.rolling(goog['Log_Ret'],
                                      window=252).std()*np.sqrt(252)

%matplotlib inline
goog[['Close', 'Volatility']].plot(subplots=True, color='blue', figsize=(8, 6))
