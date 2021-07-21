import time, mmap, random, os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rj3(file, j, b):
    f = open(file, encoding='Latin-1')
    f_length = len(f.read())
    count = 0
    f = open(file, 'rb', buffering=b)
    t1 = time.time()
    for i in range(j):
        p = int(random.random() * (f_length-1))
        f.seek(p)
        r = f.read(1)
        count += 1
        try:
            a = r.decode()
        except:
            a = 0
        while a != '\n':
            r = f.read(1)
            count += 1
            try:
                a = r.decode()
            except:
                a = 0
    t2 = time.time()
#    print(count)
    return t2-t1, count


def rj4(file, j, b):
    f = open(file, encoding='Latin-1')
    f_length = len(f.read())
    count = 0
    f = open(file, 'r', buffering = b)
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    t1 = time.time()
    for i in range(j):
        p = int(random.random() * (f_length - 1))
        m.seek(p)
        try:
            r = m.readline()
            count += len(r)
        except:
            r = f.readline()
            count += len(r)
    t2 = time.time()
#    print(count)
    return t2 - t1, count

def buffersize(file, n):
    t3, t4 = [], []
    for i in range(11):
        x3, y3 = rj3(file, j=1000, b=n)
        x4, y4 = rj4(file, j=1000, b=n)
        
        t3.append(x3)
        t4.append(x4)

    a3 = 1000*sum(t3)/len(t3)
    a4 = 1000*sum(t4)/len(t4)
    result = [a3, a4, y4]
    return result


buffersizes = []
t1, t2 = [], []

filesizes = []
path = "/Users/testing/Desktop/imdb" 

result = {}

for filename in os.listdir(path):
    if filename.endswith('.csv'):
        file = '/Users/testing/Desktop/imdb/'+filename
        print(file)
        s = os.stat(file).st_size 
        numbers_sizes = (10**exp for exp in range(1, 10))
        for n in numbers_sizes:
            print(n)
            buffersizes.append(n)
            t = buffersize(file, n)
            print(t)
            t1.append(t[0])
            t2.append(t[1])
            filesizes.append(s)
    else:
        continue
        
result['filesize'] = filesizes
result['BufferSize'] = buffersizes
result['Method3'] = t1
result['Method4'] = t2


df = pd.DataFrame(result)
optbuffer3 = df.loc[df.groupby(['filesize'])['Method3'].idxmin()][['filesize', 'BufferSize', 'Method3']]
optbuffer4 = df.loc[df.groupby(['filesize'])['Method4'].idxmin()][['filesize', 'BufferSize', 'Method4']]

optbuffer3.plot(kind='line',x='filesize',y='BufferSize', title='Optimal Buffer Size Method3',legend = True, style = 'x-', logx=True, logy=True)
optbuffer4.plot(kind='line',x='filesize',y='BufferSize', title='Optimal Buffer Size Method4',legend = True, style ='>-', color='red', logx=True, logy=True)

plt.show()
