import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn import preprocessing

data = pd.read_csv('newfooddata3.csv')
print(data.head)

df = data.groupby('State').size()
print(df)
sb.countplot(data=data,x=data['State'], label="Count")
plt.show()

'''
    Create Subsets of Diffent Regions in US.
    West, East, South, Midwest

westCoast = data.loc[data['State'].isin(['California', 'Washington', 'Oregon', 'Hawaii', 
                                         'Nevada', 'Arizona', 'Alaska'])]

eastCoast = data.loc[data['State'].isin(['Connecticut', 'Delaware', 'Florida', 
                                         'Georgia','Maine', 'Maryland', 'Massachusetts',
                                         'New Hampshire','New Jersey', 'New York', 
                                         'Pennysylvania'])]

southSide = data.loc[data['State'].isin(['Alabama', 'Arkansas', 'Delaware', 'Florida', 
                                        'Kentucky', 'Louisiana', 'Maryland', 'Mississippi', 
                                        'North Carolina', 'Oklahoma', 
                                        'South Carolina', 'Tennessee', 
                                        'Texas', 'Virginia', 'West Virginia'])]

midwest = data.loc[data['State'].isin(['Minnesota', 'Wisconsin', 'Illinois', 'Ohio'
                                       'Indiana', 'Michigan', 'Missouri', 'Iowa'
                                       'Kansas', 'Nebraska', 'North Dakota','South Dakota'])]
'''

print(df)
westCoast = ['California', 'Washington', 'Oregon', 'Hawaii', 
            'Nevada', 'Arizona', 'Alaska']

eastCoast = ['Connecticut', 'Delaware', 'Florida', 
             'Georgia','Maine', 'Maryland', 'Massachusetts',
             'New Hampshire','New Jersey', 'New York', 'Pennysylvania']

southRegion = ['Alabama', 'Arkansas', 'Delaware', 'Florida', 
                'Kentucky', 'Louisiana', 'Maryland', 'Mississippi', 
                'North Carolina', 'Oklahoma', 'South Carolina', 
                'Tennessee', 'Texas', 'Virginia', 'West Virginia']

midWest = ['Minnesota', 'Wisconsin', 'Illinois', 'Ohio'
            'Indiana', 'Michigan', 'Missouri', 'Iowa'
            'Kansas', 'Nebraska', 'North Dakota','South Dakota']
sample = data
sample.insert(3, "Region", 'NA', False)

for row in sample.index:
    if sample.loc[row,'State'] in westCoast:
        sample.loc[row,'Region'] = 'West Coast'
    elif sample.loc[row,'State'] in eastCoast:
        sample.loc[row,'Region'] = 'East Coast'
    elif sample.loc[row, 'State'] in southRegion:
        sample.loc[row,'Region'] = 'South Side'
    elif sample.loc[row, 'State'] in midWest:
        sample.loc[row, 'Region'] = 'Midwest'
        
label_encoder = preprocessing.LabelEncoder()
sample['Region'] = label_encoder.fit_transform(sample['Region'])
sample['Region'].unique()
        