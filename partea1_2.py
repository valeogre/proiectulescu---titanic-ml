import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read data from the train csv file
train_data_in = pd.read_csv('train.csv')

# determine the number of columns of the file
columns_num = train_data_in.shape[1]
# print(f'Number of columns is: {columns_num}')

# determine the data types of each column
data_types = []
for column in train_data_in.columns:
    data_types.append((column, train_data_in[column].dtype))
# print('\nThe types of data of each column:')
# for column, dtype in data_types:
#    print(f'{column}: {dtype}')

# number of missing values of each column
missing_val = []
for col in train_data_in.columns:
    missing_val.append((col, train_data_in[col].isnull().sum()))

# print('\nNumber of missing values for each column:')
# for column, miss in missing_val:
#    print(f'{column}:{miss}')

# number of lines
rows_num = train_data_in.shape[0]
# print(f'\nNumber of rows is: {rows_num}')

# number of duplicate lines
duplicated_lines = train_data_in.duplicated().sum()
# print(f'\nNumber of duplicate lines: {duplicated_lines}')

# number of passangers that survived and of the ones that died
survived = train_data_in['Survived'].sum()
didnt_survive = rows_num - survived
# percentage of the people that survived or died
percentage_surv = 100 * survived / rows_num
percentage_died = 100 * didnt_survive / rows_num
print(f'Survived: {percentage_surv:.4f}%\n')
print(f'Died: {percentage_died:.4f}%\n')

# find the percent of passengers for every Pclass
class_count = train_data_in['Pclass'].value_counts()
class_perc = 100 * class_count / rows_num

for pclass, perc in class_perc.items():
    print(f'Class {pclass}: {perc:.4f}%\n')

# determine the number of males on ship
count_men = train_data_in[train_data_in['Sex'] == 'male'].shape[0]
percentage_men = 100 * count_men / rows_num
print(f'Male: {percentage_men:.4f}%\n')

# determine the number of females on ship
count_female = train_data_in[train_data_in['Sex'] == 'female'].shape[0]
percentage_women = 100 * count_female / rows_num
print(f'Female: {percentage_women:.4f}%\n')

#grpahic charts
# the rates of survival
x_survival = np.array(["survived", "died"])
y_survival = np.array([percentage_surv, percentage_died])

plt.figure()
plt.bar(x_survival, y_survival)
plt.show()

# percents of pessengers in every class
x_class = np.array(["Class 1", "Class 2", "Class 3"])
y_class = np.array([class_perc[1], class_perc[2], class_perc[3]])

plt.figure()
plt.bar(x_class, y_class)
plt.show()

#male or female
x_sex = np.array(["Male", "Female"])
y_sex = np.array([percentage_men, percentage_women])

plt.figure()
plt.bar(x_sex, y_sex)
plt.show()