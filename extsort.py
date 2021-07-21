
# %load merge-sort.py
#!/usr/bin/env python
import pandas as pd
from math import log
import time, os
from rrmerge2 import write2_4

def merge(sub_l, d):
    m = []
    sub_l1 = []
    j = 0
    sub_l2 = []
    while j <= len(sub_l)/d:
        try:
            for i in range(d):
                ref = i+j*d
                m.append(sub_l[ref].iloc[0])
                sub_l[ref] = sub_l[ref].drop(sub_l[ref].index[0])
        except:
            pass
        m = pd.DataFrame(m)
        while not m.empty:
            m = m.sort_values(by=f.columns[k], ascending=False)
            origin_ref = m.iloc[0]['ref']
            sub_l1.append(m.iloc[0])
            sub_l1[-1]['ref'] = j
            if not sub_l[origin_ref].empty:
                m = m.append(sub_l[origin_ref].iloc[0])
                sub_l[origin_ref] = sub_l[origin_ref].drop(sub_l[origin_ref].index[0])
            m = m.drop(m.index[0])
            m = pd.DataFrame(m)
        sub_l1 = pd.DataFrame(sub_l1)
#        sub_l2.append(sub_l1)
        sub_l2 = write2_4(sub_l1)
        sub_l1 = []
        m = []
        j = j + 1
    return sub_l2

path = "/Users/testing/Desktop/small" 
result = {}

for filename in os.listdir(path): 
    if filename.endswith('.csv'): 
        file = '/Users/testing/Desktop/small/'+filename
        f = pd.read_csv(file, error_bad_lines=False)
        s = os.stat(file).st_size
        print(file)
        numbers_sizes = (10**exp for exp in range(1, 5))
        result1 = []
        b = 10**4
        d = 10**3

        k = 0
        l = []
        sub_l = []
        i = 0
        
        t1 = time.time()
        while i <= len(f):
            f1 = f[i:i+b].sort_values(by=f.columns[k], ascending=False)
            f1['ref'] = int(i/b)
            sub_l.append(f1)
            i = i + b
        
        f1 = f[i-b:len(f)].sort_values(by=f.columns[k], ascending=False)
        f1['ref'] = int((i-b)/b)
        sub_l.append(f1)
        l.append(sub_l)
        
        for i in range(int(log(len(f), b))):
            sub_l1 = merge(l[-1], d)
            l.append(sub_l1)

        t2 = time.time()
        result1.append((t2-t1)*1000)
        result[s]=result1

print(result)


# In[ ]:





# In[27]:


import pandas as pd

m = pd.DataFrame(result)
m.index = range(1,len(m) + 1)
print(m)


# In[8]:

'''
msize = []
for n in (10**exp for exp in range(1, 10)):
    msize.append(n)
'''

# In[9]:


#m['M']=msize


# In[15]:





# In[28]:

'''
import numpy as np
import matplotlib.pyplot as plt
m.plot()
plt.title('Multi-way merge performance over Different d (M=10^4)')
plt.xlabel('d size (10**n)')
plt.ylabel('Running time (milebyte)')

plt.show()
'''

# 
