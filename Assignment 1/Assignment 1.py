# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:35:01 2022

@author: Akanksha N Shenoy
"""

import pandas as pd

dataset = pd.read_csv("Data.csv")
sal_class = []


i = 0

while i < 10:
    sal_data = dataset['Salary'][i]
    
    if sal_data >= 70000:
        sal_class.append("Class 0")
    elif sal_data >= 60000:
        sal_class.append("Class 1")
    elif sal_data >= 4800:
        sal_class.append("Class 2")
    else:
        sal_class.append("")
        
    i += 1
dataset["Salary_Class"] = sal_class
#print(dataset)

c0 = len(dataset[dataset['Salary_Class'] == 'Class 0'])
c1 = len(dataset[dataset['Salary_Class'] == 'Class 1'])
c2 = len(dataset[dataset['Salary_Class'] == 'Class 2'])

print(f'Class 0 = {c0} , Class 1 = {c1} ,Class 2 = {c2}')

monthwise_age = dataset['Age']*12
dataset['Age_converted'] = monthwise_age

print(dataset)