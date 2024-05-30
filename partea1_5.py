import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read data from the csv file
train_data_in = pd.read_csv('train.csv')

# empty list for the age category
age_cat = []

# go through the elements of the Age collumn and add to 
# the list the right interval of age
for age in train_data_in['Age']:
    if pd.isnull(age):
        age_cat.append("none")
    elif age <= 20:
        age_cat.append("[0,20]")
    elif age <= 40:
        age_cat.append("[21,40]")
    elif age <= 60:
        age_cat.append("[41,60]")
    else:
        age_cat.append("[61,max]")

# add the list as a column to the CSV file
train_data_in['Age_Category'] = age_cat
train_data_in.to_csv('train_data_age_cat.csv', index = False)

# graphic for the age categories
plt.title("Number of pessengers for each age category")
age_category = train_data_in['Age_Category'].value_counts()
age_category.plot(kind = 'bar')
plt.figure()
plt.show()
