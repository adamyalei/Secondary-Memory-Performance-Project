#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# %load rrmerge2_123.py
'''
reading with implementation 2
'''

import time
import mmap


def write1_2():
    outf = open(outfile,'wb',0)
    with open(filename1) as fp1, open(filename2) as fp2:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                if r1 or r2:
                    a = r1+r2
                    for i in a:
                        outf.write(i.encode())
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            outf.close()

def write2_2():
    outf = open(outfile,'w')
    with open(filename1) as fp1, open(filename2) as fp2:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()

                if r1 or r2:
                    a = r1+r2
                    outf.writelines(a)
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            outf.close()

def write3_2():
    outf = open(outfile,'w',buffering=10**8)
    with open(filename1) as fp1, open(filename2) as fp2:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                if r1 or r2:
                    a = r1+r2
                    for i in a:
                        outf.write(i)
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            outf.close()

def write4_2():
    #outf = open(outfile,'w',b)
    #m = mmap.mmap(outf.fileno(),0)
    with open(filename1) as fp1, open(filename2) as fp2:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                if r1 or r2:
                    a = r1+r2
                    b = b+len(a)
                    m = mmap.mmap(-1,buffering=10**4)
                    m.write(a.encode())
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            #outf.close()


# In[ ]:


# %load rrmerge2_123.py
'''
reading with implementation 2
'''

import time
import mmap


def write1_3():
    outf = open(outfile,'wb',0)
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                if r1 or r2 or r3:
                    a = r1+r2+r3
                    for i in a:
                        outf.write(i.encode())
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            outf.close()

def write2_3():
    outf = open(outfile,'w')
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                if r1 or r2 or r3:
                    a = r1+r2+r3
                    outf.writelines(a)
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            outf.close()

def write3_3():
    outf = open(outfile,'w',buffering=10**8)
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                if r1 or r2 or r3:
                    a = r1+r2+r3
                    for i in a:
                        outf.write(i)
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            outf.close()

def write4_3():
    #outf = open(outfile,'w',b)
    #m = mmap.mmap(outf.fileno(),0)
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                if r1 or r2 or r3:
                    a = r1+r2+r3
                    b = b+len(a)
                    m = mmap.mmap(-1,b=10**4)
                    m.write(a.encode())
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            #outf.close()


# In[ ]:


# %load rrmerge2_123.py
'''
reading with implementation 2
'''

import time
import mmap


def write1_4():
    outf = open(outfile,'wb',0)
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3, open(filename4) as fp4:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                r4 = fp4.readline()
                if r1 or r2 or r3 or r4:
                    a = r1+r2+r3+r4
                    for i in a:
                        outf.write(i.encode())
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            fp4.close()
            outf.close()

def write2_4():
    outf = open(outfile,'w')
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3, open(filename4) as fp4:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                r4 = fp4.readline()            
                if r1 or r2 or r3 or r4:
                    a = r1+r2+r3+r4
                    outf.writelines(a)
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            fp4.close()        
            outf.close()

def write3_4():
    outf = open(outfile,'w',buffering=10**8)
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3, open(filename4) as fp4:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                r4 = fp4.readline()
                if r1 or r2 or r3 or r4:
                    a = r1+r2+r3+r4
                    for i in a:
                        outf.write(i)
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            fp4.close()
            outf.close()

def write4_4():
    #outf = open(outfile,'w',b)
    #m = mmap.mmap(outf.fileno(),0)
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3, open(filename4) as fp4:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                r4 = fp4.readline()            
                if r1 or r2 or r3 or r4:
                    a = r1+r2+r3+r4
                    b = b+len(a)
                    m = mmap.mmap(-1,b=10**4)
                    m.write(a.encode())
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            fp4.close()
            #outf.close()


# In[ ]:


# %load rrmerge2_123.py
'''
reading with implementation 2
'''

import time
import mmap


def write1_5():
    outf = open(outfile,'wb',0)
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3, open(filename4) as fp4, open(filename5) as fp5:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                r4 = fp4.readline()
                r5 = fp5.readline()
                if r1 or r2 or r3 or r4 or r5:
                    a = r1+r2+r3+r4+r5
                    for i in a:
                        outf.write(i.encode())
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            fp4.close()
            fp5.close()
            outf.close()

def write2_5():
    outf = open(outfile,'w')
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3, open(filename4) as fp4, open(filename5) as fp5:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                r4 = fp4.readline()            
                r5 = fp5.readline()
                if r1 or r2 or r3 or r4 or r5:
                    a = r1+r2+r3+r4+r5
                    outf.writelines(a)
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            fp4.close()
            fp5.close()
            outf.close()

def write3_5():
    outf = open(outfile,'w',buffering=10**8)
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3, open(filename4) as fp4, open(filename5) as fp5:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                r4 = fp4.readline()
                r5 = fp5.readline()
                if r1 or r2 or r3 or r4 or r5:
                    a = r1+r2+r3+r4+r5
                    for i in a:
                        outf.write(i)
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            fp4.close()
            fp5.close()
            outf.close()

def write4_5():
    #outf = open(outfile,'w',b)
    #m = mmap.mmap(outf.fileno(),0)
    with open(filename1) as fp1, open(filename2) as fp2, open(filename3) as fp3, open(filename4) as fp4, open(filename5) as fp5:
        try:
            t1 = time.time()
            while True:
                r1 = fp1.readline()
                r2 = fp2.readline()
                r3 = fp3.readline()
                r4 = fp4.readline()            
                r5 = fp5.readline()
                if r1 or r2 or r3 or r4 or r5:
                    a = r1+r2+r3+r4+r5
                    b = b+len(a)
                    m = mmap.mmap(-1,b=10**4)
                    m.write(a.encode())
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            fp1.close()
            fp2.close()
            fp3.close()
            fp4.close()
            fp5.close()
            #outf.close()


# In[ ]:


filename1 = '/Users/testing/Desktop/big/title copy.csv'
filename2 = '/Users/testing/Desktop/big/char_name copy.csv'
filename3 = '/Users/testing/Desktop/big/name copy.csv'
filename4 = '/Users/testing/Desktop/big/person_info copy.csv'
filename5 = '/Users/testing/Desktop/big/movie_info copy.csv'
outfile = '/Users/testing/Desktop/test.csv'

k = [2,3,4,5]
print(k)
t1 = [write1_2(), write1_3(), write1_4(), write1_5()]
t2 = [write2_2(), write2_3(), write2_4(), write2_5()]
t3 = [write3_2(), write3_3(), write3_4(), write3_5()]
t4 = [write4_2(), write4_3(), write4_4(), write4_5()]

print(t1, t2, t3, t4)


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np

l1=plt.plot(k,t1,'ro-',label='Method1')
l2=plt.plot(k,t2,'g+-',label='Method2')
l3=plt.plot(k,t3,'b^-',label='Method3')
l4=plt.plot(k,t4,'y>-',label='Method4')


plt.title('Combined R&W Running time between 4 methods (Big Files)')
plt.xlabel('Number of streams (k)')
plt.ylabel('Running time (mileseconds)')
plt.legend()
plt.savefig('tmp.pdf', bbox_inches='tight')
plt.show()


# In[ ]:




