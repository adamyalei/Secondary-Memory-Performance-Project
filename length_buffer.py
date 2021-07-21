#!/usr/bin/env python
# coding: utf-8

# In[43]:


import time, mmap, os, io
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

outfile = '/Users/testing/Desktop/test.csv'

def read3(file, b=0):
    f = open(file, 'rb', buffering=b)
    count = 0
    t1 = time.time()
    r = f.read(1)
    count += 1
    while r:
        if r != None:
            r = f.read(1)
            count += 1
        else:
            break
    t2 = time.time()
    f.close()
#    print(count)
    return t2-t1, count

def write3(file, b):
    outf = open(outfile,'w',b)
    with open(file) as fp:
        try:
            t1 = time.time()
            while True:
                r1 = fp.readline()
                if r1:
                    for i in r1:
                        outf.write(i)
                else:
                    break
        finally:
            t2 = time.time()
#            print(t2-t1)
            return t2-t1
            fp.close()
            outf.close()

                    
def read4(file, offset=0, size=None, b=1024*1024):
    file_obj = open(file)
    size = size or os.fstat(file_obj.fileno()).st_size - offset
    count = 0
    t1 = time.time()
    if size != 0 and offset % mmap.ALLOCATIONGRANULARITY == 0:
        target = mmap.mmap(file_obj.fileno(), length=size,
                           offset=offset,
                           access=mmap.ACCESS_READ)
    else:
        target = file_obj
        target.seek(offset)
    while size > 0:
        data = target.read(b)
        count += len(data)
        size -= len(data)
    if target is file_obj:
        file_obj.seek(offset)
    else:
        target.close()
    t2 = time.time()
    file_obj.close()
#    print(count)
    return t2-t1, count

def write4(file, b):
    #outf = open(outfile,'w',b)
    #m = mmap.mmap(outf.fileno(),0)
    with open(file) as fp:
        try:
            t1 = time.time()
            while True:
                r1 = fp.readline()
                if r1:
                    b = b+len(r1)
                    m = mmap.mmap(-1,b)
                    m.write(r1.encode())
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
#            print(t2-t1)
            fp.close()
            #outf.close()


# In[44]:


# Determine the optimal buffer size
def buffersize(file, n):
    rd3, rd4, wt3, wt4 = [], [], [], []
    for i in range(20):
#        r3, y3 = read3(file, b=n)
#        w3 = write3(file, n)
#        r4, y4 = read4(file, b=n)
        w4 = write4(file, n)
        
#        rd3.append(r3)
#        rd4.append(r4)
#        wt3.append(w3)
        wt4.append(w4)

#    a3 = 1000*sum(rd3)/len(rd3)
#    a4 = 1000*sum(rd4)/len(rd4)
#    b3 = 1000*sum(wt3)/len(wt3)
    b4 = 1000*sum(wt4)/len(wt4)
#    result = [a3, a4, b3, b4, y4]
    result = [b4, y4]
    return result


# In[47]:



buffersizes = []
r3, r4, w3, w4, t3, t4 = [], [], [], [], [], []
filesizes = []
path = "/Users/testing/Desktop/imdb" 
files= os.listdir(path)
result = {}

for filename in files: 
    if filename.endswith('.csv'): 
        file = '/Users/testing/Desktop/imdb/'+filename
        s = os.stat(file).st_size
        print(file)
        numbers_sizes = (10**exp for exp in range(1, 10))
        for n in numbers_sizes:
            print(n)
            buffersizes.append(n)
            t = buffersize(file, n)
            print(t)
            w4.append(t[0])
            filesizes.append(t[1])
            '''
            r3.append(t[0])
            r4.append(t[1])
            w3.append(t[2])
            w4.append(t[3])
            tt3 = t[0] + t[2]
            tt4 = t[1] + t[3]
            t3.append(tt3)
            t4.append(tt4)
            filesizes.append(t[4])
            '''


# In[46]:



result['filesize'] = filesizes
result['BufferSize'] = buffersizes
result['Method3-Read'] = r3
result['Method4-Read'] = r4
result['Method3-Write'] = w3
result['Method4-Write'] = w4
result['Method3-Total'] = t3
result['Method4-Total'] = t4

df = pd.DataFrame(result)
optbuffer3r = df.loc[df.groupby(['filesize'])['Method3-Read'].idxmin()][['filesize', 'BufferSize', 'Method3-Read']]
optbuffer4r = df.loc[df.groupby(['filesize'])['Method4-Read'].idxmin()][['filesize', 'BufferSize', 'Method4-Read']]

optbuffer3w = df.loc[df.groupby(['filesize'])['Method3-Write'].idxmin()][['filesize', 'BufferSize', 'Method3-Write']]
optbuffer4w = df.loc[df.groupby(['filesize'])['Method4-Write'].idxmin()][['filesize', 'BufferSize', 'Method4-Write']]

optbuffer3 = df.loc[df.groupby(['filesize'])['Method3-Total'].idxmin()][['filesize', 'BufferSize', 'Method3-Total']]
optbuffer4 = df.loc[df.groupby(['filesize'])['Method4-Total'].idxmin()][['filesize', 'BufferSize', 'Method4-Total']]

optbuffer3r.plot(kind='line',x='filesize',y='BufferSize', title = 'Method3 Reading Optimal Buffer Size', legend = False, style = 'x-', logx = True, logy=True)
optbuffer4r.plot(kind='line',x='filesize',y='BufferSize', title = 'Method4 Reading Optimal Buffer Size', legend = 0, style ='>-', color='red', logx = True, logy=True)

optbuffer3w.plot(kind='line',x='filesize',y='BufferSize', title = 'Method3 Writing Optimal Buffer Size', legend = 0, style = 'x-', logx = True, logy=True)
optbuffer4w.plot(kind='line',x='filesize',y='BufferSize', title = 'Method3 Writing Optimal Buffer Size', legend = 0, style ='>-', color='red', logx = True, logy=True)

optbuffer3.plot(kind='line',x='filesize',y='BufferSize', title = 'Method3 Optimal Buffer Size', legend = 0, style = 'x-', logx = True, logy=True)
optbuffer4.plot(kind='line',x='filesize',y='BufferSize', title = 'Method4 Optimal Buffer Size', legend = 0, style ='>-', color='red', logx = True, logy=True)

plt.show()


# In[ ]:




