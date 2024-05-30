import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read data from the train csv file
train_data_in = pd.read_csv('train.csv')

# number of lines
rows_num = train_data_in.shape[0]

# add to a list the columns that have missing values
columns_missing_values = []
for column in train_data_in.columns:
    if train_data_in[column].isnull().sum() > 0:
        columns_missing_values.append(column)
    
print('Columns with missing values:', columns_missing_values)

# create a list that stores the column's name, the number of missing
# elements and the proportion
missing_details = []
for column in columns_missing_values:
    missing_data = train_data_in[column].isnull().sum()
    proportion = 100 * missing_data / rows_num
    missing_details.append((column, missing_data, proportion)) 
print('Columns with missing values:',missing_details)

# dfor each column with missing values, I check what percentage the number of missing 
# values ​​represents from the number of data in the survived column
for column in columns_missing_values:
    print(f'{column}')
    for survived_class in [0, 1]:
        count_values = train_data_in[train_data_in['Survived'] == survived_class].shape[0]
        missing_count = train_data_in[train_data_in['Survived'] == survived_class][column].isnull().sum()
        try:
            percentage_missing_class = 100 * missing_count / count_values
        except ZeroDivisionError:
            percentage_missing_class = 0
        print(f'{survived_class}: {percentage_missing_class:.2f}%\n')