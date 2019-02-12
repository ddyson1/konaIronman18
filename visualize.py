import pandas as pd 
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv') 
data.sort_values('|__div_rank', inplace=True)

data.plot('div_rank,swim')

print(list(data.columns.values))
print(type(data))

plt.show()