import matplotlib.pyplot as plt
import pandas as pd
import os
expenditures = pd.read_csv(os.path.join(os.path.dirname(__file__), 'assets', 'eExpenditures_2021.csv'))

most_expensive = expenditures.nlargest(10, 'CheckAmt')
print(most_expensive)
