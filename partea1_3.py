import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read data from the train csv file
train_data_in = pd.read_csv('train.csv')

# determine the number of columns of the file
columns_num = train_data_in.shape[1]
print(f'Number of columns is: {columns_num}')

# determine the data types of each column
data_types = []
for column in train_data_in.columns:
    data_types.append((column, train_data_in[column].dtype))
print('\nThe types of data of each column:')
for column, dtype in data_types:
    print(f'{column}: {dtype}')

# number of missing values of each column
missing_val = []
for col in train_data_in.columns:
    missing_val.append((col, train_data_in[col].isnull().sum()))

print('\nNumber of missing values for each column:')
for column, miss in missing_val:
    print(f'{column}:{miss}')

# number of lines
rows_num = train_data_in.shape[0]
print(f'\nNumber of rows is: {rows_num}')

# number of duplicate lines
duplicated_lines = train_data_in.duplicated().sum()
print(f'\nNumber of duplicate lines: {duplicated_lines}')
