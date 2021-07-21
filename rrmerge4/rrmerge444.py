import time
import mmap
import os
#change the filesize limit to the line length limit

def combined4(file1,file2,file3,file4,b,bw):
    #outf = open(outfile,'w',bw)
    with open(file1, 'rb', buffering=0) as f1,open(file2, 'rb', buffering=0) as f2,open(file3, 'rb', buffering=0) as f3, open(file4, 'rb', buffering=0) as f4:
        m1 = mmap.mmap(f1.fileno(), 0, access=mmap.ACCESS_READ)
        m2 = mmap.mmap(f2.fileno(), 0, access=mmap.ACCESS_READ)
        m3 = mmap.mmap(f3.fileno(), 0, access=mmap.ACCESS_READ)
        m4 = mmap.mmap(f4.fileno(), 0, access=mmap.ACCESS_READ)
        try:
            t1 = time.time()
            while True:
                
                l1 = m1.readline()
                ll1 = len(l1)
                r1 = b''
                
                e1 = ll1//b
                if e1:
                    m1.seek(-ll1,1)
                    y1 = ll1-e1*b
                    for i in range(e1):
                        c1 = m1.read(b)
                        r1 += c1
                    if y1:
                        r1 += m1.read(y1)                            
                else:
                    r1 = l1

                l2 = m2.readline()
                ll2 = len(l2)
                r2 = b''
                
                e2 = ll2//b
                if e2:
                    m2.seek(-ll2,1)
                    y2 = ll2-e2*b
                    for i in range(e2):
                        c2 = m2.read(b)
                        r2 += c2
                    if y2:
                        r2 += m2.read(y2)                           
                else:
                    r2 = l2
                    
                l3 = m3.readline()
                ll3 = len(l3)
                r3 = b''
                
                e3 = ll3//b
                if e3:
                    m3.seek(-ll3,1)
                    y3 = ll3-e3*b
                    for i in range(e3):
                        c3 = m3.read(b)
                        r3 += c3
                    if y3:
                        r3 += m3.read(y3)
                else:
                    r3 = l3
    
                
                if r1 or r2 or r3 or r4:
                    a = str(r1+r2+r3+r4)
                    bw += len(a)
                    m = mmap.mmap(-1,bw)
                    m.write(a)
                else:
                    break

                e4 = ll4//b
                if e4:
                    m4.seek(-ll4,1)
                    y4 = ll4-e4*b
                    for i in range(e4):
                        c4 = m4.read(b)
                        r4 += c4
                    if y4:
                        r4 += m4.read(y4)
                else:
                    r4 = l4
    
                
                if r1 or r2 or r3 or r4:
                    a = str(r1+r2+r3+r4)
                    bw += len(a)
                    m = mmap.mmap(-1,bw)
                    m.write(a)
                else:
                    break
        finally:
            t2 = time.time()
            return t2-t1
            f1.close()
            f2.close()
            f3.close()
            f4.close()
            #outf.close()
