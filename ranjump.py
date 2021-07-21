import time, mmap, random, os, io
import numpy as np

def rj1(file, j):
    f = open(file)
    f_length = len(f.read())
    count = 0
    f = open(file, 'rb', buffering=0)
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
    return t2-t1, count


def rj2(file, j):
    f = open(file)
    f_length = len(f.read())
    count = 0
    f = open(file, encoding='Latin-1')
    t1 = time.time()
    for i in range(j):
        p = int(random.random() * (f_length-1))
        f.seek(p)
        try:
            r = f.readline()
            count += len(r)
        except:
            r = f.readline()
            count += len(r)
    t2 = time.time()
    return t2 - t1, count


def rj3(file, j, b):
    f = open(file)
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
    return t2-t1, count


def rj4(file, j, b):
    f = open(file)
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
    return t2 - t1, count

# Iterate all files
path = "/Users/testing/Desktop/imdb"

result = {}

LOOP = 1000

for filename in os.listdir(path):
    if filename.endswith('.csv'):    
        file = '/Users/testing/Desktop/imdb/'+filename
        print(filename)
        s = os.stat(file).st_size
        t1, t2, t3, t4 = [], [], [], []
        a1, y1 = rj1(file, LOOP)
        a2, y2 = rj2(file, LOOP)
        a3, y3 = rj3(file, LOOP, b=100)
        a4, y4 = rj4(file, LOOP, b=10**4)
        result[s] = [a1, a2, a3, a4]
    else:
        continue

import matplotlib.pyplot as plt

result1 = sorted(result.items())

n, t1, t2, t3, t4 = [], [], [], [], []

for i in result1: 
    n.append(i[0])
    t1.append(i[1][0]*1000)
    t2.append(i[1][1]*1000)
    t3.append(i[1][2]*1000)
    t4.append(i[1][3]*1000)
    
l1=plt.plot(n,t1,'ro--',label='Method 1')
l2=plt.plot(n,t2,'g+--',label='Method 2')
l3=plt.plot(n,t3,'b^--',label='Method 3')
l4=plt.plot(n,t4,'y>--',label='Method 4')

plt.title('Random Jump Comparison between 4 methods j=1000')
plt.xlabel('File size (byte)')
plt.ylabel('Reading time (mileseconds)')
plt.xscale('log')
plt.legend()
plt.show()
