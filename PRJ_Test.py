import pandas as pd
#%matplotlib inline
#%pylab inline
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')

dataset = pd.read_csv('houses_to_rent_v2.csv', sep=';')
print(dataset.head().T)

print(dataset.groupby('city')['city'].count())