import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.model_selection import train_test_split
from sklearn import metrics

file = (r"houses_to_rent_v2.csv")
df = pd.read_csv(file)
cleanup_nums = {"animal":     {"not acept": 0, "acept": 1},
                "furniture": {"not furnished": 0, "furnished": 1}}

df.replace(cleanup_nums, inplace=True)
print(df.head())
