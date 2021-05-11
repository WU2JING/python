from math import sqrt
import math
from numpy import unique
def cal_dis(k=[],j=[]):
    a1=pow(k[0]-j[0],2)
    b1=pow(k[1]-j[1],2)
    c1=pow(k[2]-j[2],2)
    return sqrt(a1+b1+c1)

def cal_ang(a,b,c):
    theta=(pow(b,2)+pow(c,2)-pow(a,2))/(2*b*c)
    return math.acos(theta)*180/(math.pi)
r=[[],[],[],[]] #计算需要4个原子的坐标,建立四个数组
kk=1
data2=open('./res.dat','w')
while True:
    r=[[],[],[],[]]
    if kk >50:             #当前目录下50个lammps输出文件
        break    
    file1=open('data'+str(kk)+'.lmp','r') #循环读取文件
    i=0
    xx,yy,zz=[],[],[]
    while True:
        data=file1.readline()
        i+=1
        if i>=577:
            break
    
        if i>16 :
            xx.append(round((float(data.split()[2])),9))
            yy.append(round((float(data.split()[3])),9))
            zz.append(round((float(data.split()[4])),9))
    file1.close()
    xx=unique(xx)
    yy=unique(yy)
    zz=unique(zz)
#    print(len(xx),len(zz),len(yy))
#    print((xx[1]),xx[2])
    if kk<34:
        r[0].append(xx[1])
        r[0].append(yy[27])
        r[0].append(zz[1])
        r[1].append(xx[1])
        r[1].append(yy[25])
        r[1].append(zz[1])
        r[2].append(xx[2])
        r[2].append(yy[26])
        r[2].append(zz[1])
        r[3].append(xx[3])
        r[3].append(yy[26])
        r[3].append(zz[0])
    else:
        r[0].append(xx[0])
        r[0].append(yy[27])
        r[0].append(zz[1])
        r[1].append(xx[0])
        r[1].append(yy[25])
        r[1].append(zz[1])
        r[2].append(xx[1])
        r[2].append(yy[26])
        r[2].append(zz[1])
        r[3].append(xx[2])
        r[3].append(yy[26])
        r[3].append(zz[0])
#    print(r)
    pusai=math.asin((zz[1]-zz[0])/cal_dis(r[2],r[3]))
    print("r1={}".format(cal_dis(r[1],r[2]) ))
    print("r2={}".format(cal_dis(r[2],r[3]) ))
    print("afa={}".format(cal_ang(cal_dis(r[0],r[1]),cal_dis(r[1],r[2]),cal_dis(r[2],r[0]) )))
    print("pusai={}".format(cal_ang(cal_dis(r[1],r[3]),cal_dis(r[1],r[2]),cal_dis(r[2],r[3]))))
    data2.write(str(cal_dis(r[1],r[2])))
    data2.write(' ')
    data2.write(str(cal_dis(r[2],r[3])))
    data2.write(' ')
    data2.write(str(cal_ang(cal_dis(r[0],r[1]),cal_dis(r[1],r[2]),cal_dis(r[2],r[0]))))
    data2.write(' ')
    data2.write(str(cal_ang(cal_dis(r[1],r[3]),cal_dis(r[1],r[2]),cal_dis(r[2],r[3]))))
    data2.write('\n')
    kk+=1
    file1.close()
data2.close()
