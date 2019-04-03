# Sales Representative

import pandas as pd
import numpy as np
import seaborn as sns

sns.set_style('whitegrid')


def calc_commission_rate(x):
    """ Return the commission rate based on the table:
    0-90% = 2%
    91-99% = 3%
    >= 100 = 4%
    """
    if x <= .90:
        return .02
    if x <= .99:
        return .03
    else:
        return .04


print(calc_commission_rate.__doc__)


def randomPctTarget(reps, std, pct_avg, sales_target_vals, sales_target_prob):
    pct_target = np.random.normal(avg, std_dev, num_reps).round(2)
    sales_target = np.random.choice(sales_target_values, num_reps, p=sales_target_prob)

    return pct_target, sales_target


def designDFrame(pct, sales, reps):
    Df = pd.DataFrame(index=range(reps), data={'Pct_To_Target': pct,
                                               'Sales_Target': sales})

    Df['Sales'] = Df['Pct_To_Target'] * Df['Sales_Target']
    Df['Commission_Rate'] = Df['Pct_To_Target'].apply(calc_commission_rate)
    Df['Commissions_Amount'] = Df['Commission_Rate'] * Df['Sales']
    return Df


avg = 1
std_dev = .1
num_reps = 500
num_simulations = 1000
sales_target_values = [75000, 100000, 200000, 300000, 400000, 500000]
sales_target_prob = [.3, .3, .2, .1, .05, .05]

stats = []
for i in range(num_simulations):
    pct_to_target, sales_target = randomPctTarget(reps=num_reps, std=std_dev, pct_avg=avg,
                                                  sales_target_vals=sales_target_values,
                                                  sales_target_prob=sales_target_prob)

    df = designDFrame(pct=pct_to_target, sales=sales_target,reps=num_reps)
    stats.append(
        [df['Sales'].sum().round(0),
         df['Commissions_Amount'].sum().round(0),
         df['Sales_Target'].sum().round(0)])

resultDf = pd.DataFrame.from_records(stats, columns=['Sales', 'Commission_Amount', 'Sales_Target'])
resultDf.describe().style.format('{:,}')

