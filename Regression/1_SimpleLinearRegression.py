# %%  Importing the librariers 
import numpy as np 
import matplotlib.pyplot as plt 
import panda as pd 

# %%  Importing the dataset 
dataset = pd.read_csv('Data.csv')
X = dataset.iloc