import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read data from the train csv file
train_data_in = pd.read_csv('train.csv')

# determine the number of columns of the file
columns_num = train_data_in.shape[1]

# extract in a list the columns which store values that are either int64, or float64
numerical_columns = []
for column in train_data_in.columns:
    if train_data_in[column].dtype == 'int64' or train_data_in[column].dtype == 'float64':
        numerical_columns.append(column)
        
# for every column of this list I make a histogram
for column in numerical_columns:
    x = train_data_in[column]
    plt.figure()
    plt.title(f'Histogram of {column}')
    plt.hist(x)
    plt.ylabel('Frequency')
    plt.show()