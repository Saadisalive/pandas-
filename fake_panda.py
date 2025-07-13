import pandas as pd
import numpy as np

event_data = {'name': ['Player','Daima','Joker','James','Emily','Micheal','Laura','Daya','Acp','Ronaldo'],
              'score' : [12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
              'qualify' : ['yes','np','yes','no','no','yes','yes','no','no','yes']}
labels = ['a','b','c','d','e','f','g','h','i','j']

df = pd.DataFrame(event_data , index=labels)
print('Summary of the basic information about this dataframe an its data :')
print(df.info())