import matplotlib.pyplot as plt
import pandas as pd
import os
expenditures = pd.read_csv(os.path.join(os.path.dirname(__file__), 'assets', 'eExpenditures_2021.csv'))

most_expensive = expenditures.nlargest(10, 'CheckAmt')
print(most_expensive)

Department = most_expensive["Category"]
Amount = most_expensive ["CheckAmt"]

plt.bar(Department, Amount, color = 'green')
plt.xlabel('Name of the Department')
plt.ylabel('Amount invested')
plt.title('Top 10 Expenditures 2021')
plt.show()