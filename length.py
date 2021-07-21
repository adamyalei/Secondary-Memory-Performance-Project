import time, mmap, os, io

def read1(file):
    f = open(file, 'rb', buffering=0)
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
    return t2-t1, count


def read1_1(file):
    f = open(file, 'rb', buffering=0)
    t1 = time.time()
    r = f.read()
    count = len(r)
    t2 = time.time()
    print(count)
    f.close()
    return t2-t1


def read2(file):
    f = open(file)
    t1 = time.time()
    count = 0
    for line in f:
        if count <= 999999999:
            # r = f.read(len(line))
            r = f.readline()
            count += len(r)
        else:
            break
    t2 = time.time()
    print(count*2)
    f.close()
    return t2-t1


def read2_1(file):
    f = io.open(file,'r', encoding='Latin-1') #报错处
    t1 = time.time()
    count = 0
    r = f.readline()
    for i in r:
        count += 1
    while r:
        r = f.readline()
        for i in r:
            count += 1
    t2 = time.time()
    f.close()
    return t2-t1, count



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


def read3_1(file, b=0):
    f = open(file, 'rb', buffering=b)
    t1 = time.time()
    r = f.read()
    count = len(r)
    t2 = time.time()
    f.close()
    return t2-t1


def read4(file, b=2):
    f = open(file, 'rb', buffering=0)
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    t1 = time.time()
    count = 0
    l = 1
    while l != 0:
        r = m.read(b)
        count += len(r)
        l = len(r)
    print(count)
    t2 = time.time()
    f.close()
    return t2-t1


def read5(file, offset=0, size=None, chunk_size=1024*1024):
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
        data = target.read(chunk_size)
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


def read6(file, b=0):
    f = open(file, 'rb', buffering=b)
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    t1 = time.time()
    r = m.read()
    count = len(r)
    t2 = time.time()
    f.close()
    print(count)
    return t2-t1

# Iterate all files
path = "/Users/testing/Desktop/big" 
files= os.listdir(path) 

result = {}

import numpy as np

for filename in files: 
    file = '/Users/testing/Desktop/big/'+filename
    t1, t2, t3, t4 = [], [], [], []
    for i in range(5): # get average run time for 20 times
#        x1, y1 = read1(file)
        x2, y2 = read2_1(file)
#        x3, y3 = read3(file, 10**7)
#        x4, y4 = read5(file, chunk_size=10**4)
        
#        t1.append(x1)
        t2.append(x2)
#        t3.append(x3)
#        t4.append(x4)

    a1 = None
#    a1 = 1000*sum(t1)/len(t1)
    a2 = 1000*sum(t2)/len(t2)
#    a3 = 1000*sum(t3)/len(t3)
#    a4 = 1000*sum(t4)/len(t4)
    a3, a4 = None, None
    result[y2] = [a1, a2, a3, a4]
    print(result)

# Draw the graph
import matplotlib.pyplot as plt

result1 = sorted(result.items())

n, t1, t2, t3, t4 = [], [], [], []

for i in result1: 
    n.append(i[0])
    t1.append(i[1][0])
    t2.append(i[1][1])
    t3.append(i[1][2])
    t4.append(i[1][3])
'''
# Plot graphs
plt.figure(122)
plt.subplot(1,2,1)

# Plot 4 method comparison
l1=plt.plot(n,t1,'ro--',label='Method 1')
l2=plt.plot(n,t2,'g+--',label='Method 2')
l3=plt.plot(n,t3,'b^--',label='Method 3')
l4=plt.plot(n,t4,'y>--',label='Method 4')

plt.title('Comparison between 4 methods (Large files)')
plt.xlabel('File size (byte)')
plt.ylabel('Reading time (mileseconds)')
plt.legend()
'''
# Plot 3 method comparison without Method 1
ll2=plt.plot(n,t2,'g+--',label='Method 2')
ll3=plt.plot(n,t3,'b^--',label='Method 3')
ll4=plt.plot(n,t4,'y>--',label='Method 4')

plt.title('Comparison between 3 methods without Method 1 (Large files)')
plt.xlabel('File size (byte)')
plt.ylabel('Reading time (mileseconds)')
plt.legend()
plt.show()

