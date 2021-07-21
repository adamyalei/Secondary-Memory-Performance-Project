import time, mmap, os, io
import numpy as np
import matplotlib.pyplot as plt

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
#    print(count)
    f.close()
    return t2-t1, count

def read2_1(file):
    f = io.open(file,'r') #报错处
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

# Testing number of running times for average time
def multirun(p, file):
    n = []
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    avg1, avg2, avg3, avg4 = [], [], [], []
    for i in range(p):
        a = i + 1
        n.append(a)
        x1, y1 = read1(file)
        x2, y2 = read2_1(file)
        x3, y3 = read3(file, 100)
        x4, y4 = read5(file, chunk_size=100)

        t1.append(x1)
        t2.append(x2)
        t3.append(x3)
        t4.append(x4)

        a1 = 1000*sum(t1)/len(t1)
        avg1.append(a1)
        a2 = 1000*sum(t2)/len(t2)
        avg2.append(a2)
        a3 = 1000*sum(t3)/len(t3)
        avg3.append(a3)
        a4 = 1000*sum(t4)/len(t4)
        avg4.append(a4)
    print(avg1, avg2, avg3, avg4)

    l1=plt.plot(n,avg1,'r--',label='type1')
    l2=plt.plot(n,avg2,'g--',label='type2')
    l3=plt.plot(n,avg3,'b--',label='type3')
    l4=plt.plot(n,avg4,'y--',label='type4')

    plt.plot(n,avg1,'ro-',n,avg2,'g+-',n,avg3,'b^-', n,avg4, 'y>-')
    plt.title('Running time between 4 methods')
    plt.xlabel('Running times')
    plt.ylabel('Avgerage reading time (mileseconds)')
    plt.xlim(5)
    plt.ylim(ymax=2)
    plt.legend()
    plt.show()


multirun(100, '/Users/testing/Desktop/imdb/link_type.csv')
