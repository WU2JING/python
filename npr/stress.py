import os
from matplotlib import pyplot as plt 
data=open("C:\\Users\\hasee\\Desktop\\P\\file2")
i=0
j=0
stress=[]
energy=[]
while True:
    line=data.readline()
    i+=1
    j+=1
    if j>=153:
        break
    if i==1:
        y=float(line.split()[8])
        x=float(line.split()[11])
        stress.append(y)
        energy.append(x)
    if i==3:
        i=0
print(*stress,sep='\n')
print('***********************************************************************************')
print(*energy,sep='\n')    
print('***********************************************************************************')
for i in range(len(energy)):
    t=energy[i]-energy[0]
    print(t/560)
data.close()
