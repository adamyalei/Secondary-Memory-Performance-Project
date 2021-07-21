'''Medium files
k = [2,3,4,5]
t1 = [24.08962607383728, 32.816312074661255, 98.77158212661743, 336.92723274230957] 
t2 = [1.2917890548706055, 2.238011121749878, 8.818306684494019, 39.51074981689453] 
t3 = [1.1269512176513672, 1.9290728569030762, 6.772751808166504, 37.86076211929321] 
t4 = [5.507469177246094e-05, 4.982948303222656e-05, 6.29425048828125e-05, 7.104873657226562e-05]
'''
# Big files
k = [2,3,4]
t1 = [1531.395252943039, 2743.64515376091, 3727.085501909256]
t2 = [0.3442721366882324, 0.19028711318969727, 0.17616796493530273]
t3 = [0.2276020050048828, 0.1931898593902588, 0.12142181396484375]
t4 = [4.506111145019531e-05, 3.910064697265625e-05, 4.57763671875e-05]

import matplotlib.pyplot as plt
import numpy as np

l1=plt.plot(k,t1,'ro-',label='Method1')
l2=plt.plot(k,t2,'g+-',label='Method2')
l3=plt.plot(k,t3,'b^-',label='Method3')
l4=plt.plot(k,t4,'y>-',label='Method4')


plt.title('Combined R&W Running time between 4 methods (Large Files)')
plt.xlabel('Number of streams (k)')
plt.ylabel('Running time (mileseconds)')
plt.legend()
plt.savefig('cw_large.pdf', bbox_inches='tight')
plt.show()
