import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
import locale

locale.setlocale(locale.LC_ALL, '')

pv = 10000
time_horizon = 30
i = .07
additions = 10000

for year in range(time_horizon):
    ending = pv * (1 + i) + additions

    print(locale.currency(ending, grouping=True))
    pv = ending

# create future price value and some distributions with var and std i mean all of data

pv = 10000
expected_return = .09
volatility = .18
time_horizon = 30
annual_addition = 10000

print('\tReturn', '\t\tEnding Value'.rjust(18))

for year in range(time_horizon):
    # meani 0.9 luk stdsi .18lik Normal distribution
    market_return = np.random.normal(expected_return, volatility)
    fv = pv * (1 + market_return) + annual_addition
    print('\t{}'.ljust(10).format(round(market_return, 4)),
          '\t{}'.rjust(10).format(locale.currency(fv, grouping=True)))
    pv = fv

# portfolio ending market values

df = pd.DataFrame()
iterations = 5000

for x in range(iterations):
    expected_return = .09
    volatility = .18
    time_horizon = 30
    pv = 10000
    annual_investment = 10000
    stream = []
    for i in range(time_horizon):
        end = round(pv * (1 + np.random.normal(expected_return, volatility)) + annual_investment, 2)
        stream.append(end)

        pv = end
    df[x] = stream
