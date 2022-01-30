import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 


df = pd.read_csv("Advertising.csv")
X = df.drop('sales',axis=1)
y = df['sales']

