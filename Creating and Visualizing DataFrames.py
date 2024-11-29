import matplotlib.pyplot as plt
import pandas as pd
table = pd.read_csv('data.csv')
#nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()
#table.legend(alpha=0.6,bins=20)

table.isna().any().plot(kind="bar") #checks is there any missing values
plt.show()
table.dropna
table.fillna