#armchair
import os
from matplotlib import pyplot as plt 
data=open("C:\\Users\\hasee\\Desktop\\P\\file1")
i=0
j=0
strainx=[]
strainy=[]
ration=[]
while True:
    line=data.readline()
    i+=1
    j+=1
    if j>=153:
        break
    if i==2:
        y=float(line.split()[0])
        x=float(line.split()[3])
        strainx.append(x)
        strainy.append(y)
    if i==3:
        i=0
data.close()
#print(j,i)
#print(strainx)
#print(strainy)
lenth=len(strainx)
for i in range(lenth-1):
    ration.append(-(strainx[i+1]-strainx[i])/(strainy[i+1]-strainy[i]))


result=[]
for i in range(len(ration)):
    result.append(ration[i])
result.append(0)
plt.subplot(2,  1,  1) 
plt.xlabel("strainx") 
plt.ylabel("strainy") 
plt.title(" MLIP to strain")
plt.plot(strainy,strainx)
plt.axis([0,0.28,-0.1,0.05])
plt.subplot(2,  1,  2)
plt.xlabel("strainy")
plt.ylabel("pr")
plt.plot(strainy,result,'-ok')
plt.axis([0,0.28,-0.8,0.5])
plt.show()
print(*strainy,sep='\n')
print('**************************************************************************************')
print(*strainx,sep='\n')
print('**************************************************************************************')
print(*result,sep='\n')
data.close()
