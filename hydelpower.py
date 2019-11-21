#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import seaborn as sns
from plotly import __version__
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode,plot,iplot
init_notebook_mode(connected = True)
cf.go_offline()

get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import rcParams
rcParams['figure.figsize'] = 8,8
import warnings
warnings.filterwarnings('ignore')




# In[8]:


df = pd.DataFrame(index = np.arange(1,16), columns = ['PowerPlantHeight', 'WaterFlow', 'PowerGeneration'])
df.PowerPlantHeight = df.PowerPlantHeight.astype('category')
df.WaterFlow = df.WaterFlow.astype('category')
df.PowerGeneration = df.PowerGeneration.astype('category')
df.info()


# In[9]:


df.PowerPlantHeight = ['Low', 'Low', 'Medium', 'High', 'VeryHigh', 'Low', 'Medium','High','VeryLow', 'VeryHigh', 'Medium', 'Low', 'VeryHigh', 'Medium', 'VeryLow']
df.WaterFlow = ['Medium', 'VeryLow','Medium',  'Low', 'Medium', 'High', 'VeryHigh', 'Low', 'Medium','High','VeryLow', 'VeryHigh', 'Medium','High','VeryLow', ]


# In[10]:


df.PowerGeneration = df.PowerPlantHeight + df.WaterFlow
for a in df.PowerGeneration:
    if(a == 'VeryLowVeryHigh'):
        df.PowerGeneration.replace('VeryLowVeryHigh','Medium', inplace = True)
    elif(a == 'LowVeryLow'):
        df.PowerGeneration.replace('LowVeryLow','VeryLow', inplace = True)
    elif(a == 'MediumMedium'):
        df.PowerGeneration.replace('MediumMedium','Medium', inplace = True)
    elif(a == 'HighLow'):
        df.PowerGeneration.replace('HighLow','Medium', inplace = True)
    elif(a == 'VeryHighMedium'):
        df.PowerGeneration.replace('VeryHighMedium','VeryHigh', inplace = True)
    elif(a == 'LowHigh'):
        df.PowerGeneration.replace('LowHigh','Medium', inplace = True)
    elif(a == 'MediumVeryHigh'):
        df.PowerGeneration.replace('MediumVeryHigh','High', inplace = True)
    elif(a == 'MediumVeryHigh'):
        df.PowerGeneration.replace('MediumVeryHigh','High', inplace = True)
    elif(a == 'VeryLowMedium'):
        df.PowerGeneration.replace('VeryLowMedium','Low', inplace = True)
    elif(a == 'VeryHighHigh'):
        df.PowerGeneration.replace('VeryHighHigh','High', inplace = True)
    elif(a == 'MediumVeryLow'):
        df.PowerGeneration.replace('MediumVeryLow','Low', inplace = True)
    elif(a == 'LowVeryHigh'):
        df.PowerGeneration.replace('LowVeryHigh','High', inplace = True)
    elif(a == 'MediumHigh'):
        df.PowerGeneration.replace('MediumHigh','High', inplace = True)    
    elif(a == 'VeryLowVeryLow'):
        df.PowerGeneration.replace('VeryLowVeryLow','VeryLow', inplace = True)
    elif(a == 'LowMedium'):
        df.PowerGeneration.replace('LowMedium','Medium', inplace = True)

df


# In[11]:


sns.scatterplot( data = df, x = df.PowerPlantHeight, y = df.WaterFlow, hue = df.PowerGeneration, s = 100)
plt.plot(df.PowerPlantHeight,df.WaterFlow)
plt.show()


# In[ ]:




