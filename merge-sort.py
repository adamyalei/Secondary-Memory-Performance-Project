#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pandas as pd
from math import log
import time
from rrmerge2 import write2_4

file = '/Users/testing/Desktop/small/movie_link copy.csv'
f = pd.read_csv(file, error_bad_lines=False)
k = 3
b = 10000
d = b
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
#        m = pd.DataFrame(m)
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


for i in range(int(log(len(f), b))):
    sub_l1 = merge(l[-1], d)
    l.append(sub_l1)
    
t2 = time.time()
print(t2-t1, len(l[-1][0]))
