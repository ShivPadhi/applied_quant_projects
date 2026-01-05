import numpy as np

# This is part of our feature engineering for our multi-dimensional dataset used in a volatility and IV analysis project. It computes realized volatility measures over multiple horizons to use in modeling.

# Compute log returns 
df['log_returns'] = np.log(df['Close'] / df['Close'].shift(1))

# Forward 3-day realized volatility (target) 
h = 3  # horizon
r2 = df['log_returns'] ** 2
# rolling sum over h days, then shift back so row t uses r_{t+1},...,r_{t+h}
fwd_sum = r2.rolling(h).sum().shift(-h)
df['3_day_forward_rv'] = np.sqrt((252 / h) * fwd_sum)

# Backward realized volatilities (features)
for n in [3, 5, 10, 15, 20]:
    r2 = df['log_returns'] ** 2
    back_sum = r2.rolling(n).sum()
    df[f'{n}_day_backward_rv'] = np.sqrt((252 / n) * back_sum)