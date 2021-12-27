import sys
import math
import numpy as np
import pandas as pd
import numpy.linalg as LA
A     = 1.0e-10         # m
ev    = 1.602176565e-19 # J
ps    = 1.0e-12         # s
dt    = 0.001          # ps
lx    = 15.027857        # [Angstrom]
ly    = 15.027857            # [Angstrom]
area  = lx*ly*A**2     # m^2 
num=21
n=-2
a=[]
b=[]
Q=[]
step=[]
T=[]
leng=[]
while True:
    line=file2.readline()
    if len(line)==0:
         break
    n+=1
    if n>0:
        x=(float(line.split()[2])-float(line.split()[1]))/2
        Q.append(x)
        file3.write(str(x))
        file3.write('\n')
        y=(int(line.split()[0])-6000)
        step.append(y) 
        file4.write(str(y))
        file4.write('\n')
       # file5.write(str( y * 0.0005))
       # file5.write('\n')
m=-2
sum=[0.0 for i in range(num)]
while True:
    line=file1.readline()
    if len(line)==0:
         break
    m+=1
    if m>0:
         for i in range(0,num):
              sum[i]+=float(line.split()[i+1])

#print(m)
for i in range(len(sum)):
    T.append(sum[i]/m)
AA = np.vstack([step, np.ones(len(step))]).T
Q=np.array(Q)
a=LA.lstsq(AA,Q,rcond=None)[0]
#print(a[0])
slab=21
#slab=int(input('请输入slab的数量:'))
length=300.55714
#length=float(input('请输入模拟尺度的长度:'))
eps=5
#eps=int(input('请输入eps的长度'))
for i in range(slab):
    every=(length-2*eps)/slab
    oder=((length-2*eps)/slab)/2+eps+every*i
    leng.append(oder)
#print(leng)
AA = np.vstack([leng, np.ones(len(leng))]).T                                     
for i in range(len(T)):
    print(T[i])
print('***********************************************************')
for i in range(len(leng)):
    print(leng[i])
T=np.array(T)                                                                    
b=LA.lstsq(AA,T,rcond=None)[0]
A     = 1.0e-10         # m
ev    = 1.602176565e-19 # J
ps    = 1.0e-12         # s
dt    = 0.001          # ps
lx    = 15.027857        # [Angstrom]
ly    = 15.027857       # [Angstrom]
area  = lx*ly*A**2     # m^2 
jk= a[0]
dT=   b[0]
TK =  -jk/dt*ev/ps/area/(dT/A)
TK2 =  -jk/dt*ev/ps/area/(-0.09697/A)
print('***********************************************************')
print(TK)
print(TK2)
