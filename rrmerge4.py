#!/usr/bin/env python
# coding: utf-8

# In[11]:


# %load rrmerge4_123.py
import time
import mmap
import os
#change the filesize limit to the line length limit
     
from rrmerge412 import combined1 as rrm412
from rrmerge422 import combined2 as rrm422
from rrmerge432 import combined3 as rrm432
from rrmerge442 import combined4 as rrm442

from rrmerge413 import combined1 as rrm413
from rrmerge423 import combined2 as rrm423
from rrmerge433 import combined3 as rrm433
from rrmerge443 import combined4 as rrm443

from rrmerge414 import combined1 as rrm414
from rrmerge424 import combined2 as rrm424
from rrmerge434 import combined3 as rrm434
from rrmerge444 import combined4 as rrm444

file1 = '/Users/testing/Desktop/small/comp_cast_type copy.csv'
file2 = '/Users/testing/Desktop/small/kind_type copy.csv'
file3 = '/Users/testing/Desktop/small/company_type copy.csv'
file4 = '/Users/testing/Desktop/small/role_type copy.csv'

outfile = '/Users/testing/Desktop/test.csv'

t12 = rrm412(file1,file2,b = 10000)
t22 = rrm422(file1,file2,b = 10000)   
t32 = rrm432(file1,file2,b = 10000,bw =10)
t42 = rrm442(file1,file2,b = 10000,bw =10)

t13 = rrm413(file1,file2,file3,b = 10000)
t23 = rrm423(file1,file2,file3,b = 10000)   
t33 = rrm433(file1,file2,file3,b = 10000,bw =10)
t43 = rrm443(file1,file2,file3,b = 10000,bw =10)

t14 = rrm414(file1,file2,file3,file4,b = 10000)
t24 = rrm424(file1,file2,file3,file4,b = 10000)   
t34 = rrm434(file1,file2,file3,file4,b = 10000,bw =10)
t44 = rrm444(file1,file2,file3,file4,b = 10000,bw =10)


# In[12]:


k = [2,3,4]
print(k)
t1 = [t12, t13, t14]
t2 = [t22, t23, t24]
t3 = [t32,t33,t34]
t4 = [t42,t43,t44]


# In[13]:



import matplotlib.pyplot as plt
import numpy as np

l1=plt.plot(k,t1,'ro-',label='Method1')
l2=plt.plot(k,t2,'g+-',label='Method2')
l3=plt.plot(k,t3,'b^-',label='Method3')
l4=plt.plot(k,t4,'y>-',label='Method4')


plt.title('Combined R&W Running time between 4 methods (Small Files)')
plt.xlabel('Number of streams (k)')
plt.ylabel('Running time (mileseconds)')
plt.legend()
plt.savefig('tmp.pdf', bbox_inches='tight')
plt.show()


# In[14]:


print(t1,t2,t3,t4)

