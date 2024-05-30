import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data from the csv file
train_data_in = pd.read_csv('train_data_age_cat.csv')

# from the new CSV file I select the males
men_data = train_data_in[train_data_in['Sex'] == 'male']
# count the number of males that survived frokm each age category
cnt_survived = men_data[men_data['Survived'] == 1]['Age_Category'].value_counts()
# count the number of men from each age category
cnt_men = men_data['Age_Category'].value_counts()
# print the rate of survival
print(100 * cnt_survived / cnt_men)


# graphic for the age categories
plt.title("Number of men that survived for each age category")
age_category = 100 * cnt_survived / cnt_men
age_category.plot(kind = 'bar')
plt.figure()
plt.show()
