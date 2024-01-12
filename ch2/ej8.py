# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplots

plt.close('all')

college = pd.read_csv('College.csv')
college.rename({'Unnamed: 0':'College'}, axis=1, inplace=True)
college.set_index(['College'], inplace=True, verify_integrity=True)

college.loc[college['Top10perc']>50, 'Elite'] = 'Yes'
college['Elite'] = college['Elite'].fillna('No')

#sns.boxplot(x='Elite', y='Outstate', data=college);

# Bins creation

fig, ax = subplots(2,2)

college['Grad.Rate'].plot.hist(ax=ax[0,0])
college['Books'].plot.hist(ax=ax[0,1])
college['Enroll'].plot.hist(ax=ax[1,0])
college['Apps'].plot.hist(ax=ax[1,1])
