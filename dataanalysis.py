import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_csv('newfooddata3.csv')
print(data.head)

df = data.groupby('State').size()
print(df)
sb.countplot(data=data,x=data['State'], label="Count")
plt.show()

westCoast = data.loc[data['State'].isin(['California', 'Washington', 'Oregon', 'Hawaii', 
                                         'Nevada', 'Arizona', 'Alaska'])]
print(westCoast)

eastCoast = data.loc[data['State'].isin(['Connecticut', 'Delaware', 'Florida', 
                                         'Georgia','Maine', 'Maryland', 'Massachusetts',
                                         'New Hampshire','New Jersey', 'New York', 
                                         'Pennysylvania'])]
print(eastCoast)

southSide = data.loc[data['State'].isin(['Alabama', 'Arkansas', 'Delaware', 'Florida', 
                                        'Kentucky', 'Louisiana', 'Maryland', 'Mississippi', 
                                        'North Carolina', 'Oklahoma', 
                                        'South Carolina', 'Tennessee', 
                                        'Texas', 'Virginia', 'West Virginia'])]

midwest = data.loc[data['State'].isin(['Minnesota', 'Wisconsin', 'Illinois', 'Ohio'
                                       'Indiana', 'Michigan', 'Missouri', 'Iowa'
                                       'Kansas', 'Nebraska', 'North Dakota','South Dakota'])]

