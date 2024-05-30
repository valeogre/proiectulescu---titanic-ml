import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data from the csv file
train_data_in = pd.read_csv('train_data_age_cat.csv')

num_children = 0
num_adults = 0
for age in train_data_in['Age']:
    if pd.notnull(age):
        if age < 18:
            num_children += 1
        else:
            num_adults += 1
            
rows_num = train_data_in.shape[0]

child_perc = 100 * num_children / rows_num

children_survived = train_data_in[(train_data_in['Age'] < 18) & (train_data_in['Survived'] == 1)].shape[0]
adults_survived = train_data_in[(train_data_in['Age'] >= 18) & (train_data_in['Survived'] == 1)].shape[0]

child_survive_rate = 100 * children_survived /  num_children
adults_survive_rate = 100 * adults_survived / num_adults

print(f'survive rate children:{child_survive_rate:.2f}%')
print(f'survive rate adults:{adults_survive_rate:.2f}%')