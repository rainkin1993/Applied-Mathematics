import numpy as np
from pylab import *

        

def readdigital(digital):
    file=open("optdigits .tra")
    digital_array=[]
    digital_array_tem=[]
    while 1:
        line=file.readline()
        line_list=line.split(',')
        length=len(line_list)
        if not length==1:
            if int(line_list[length-1][0])==digital:
                for i in range(length-1):
                    digital_array_tem.append(int(line_list[i]))
                digital_array.append(digital_array_tem)
                digital_array_tem=[]
        if not line:
            return digital_array


def mean(array):
    d=len(array[1])
    n=len(array)
    dsum=[]
    for i in range(d):
        sum=0
        for j in range(n):
            sum=sum+array[j][i]
            dmean=float(sum)/float(n)
        dsum.append(dmean)
    for k in range(d):
        for t in range(n):
            array[t][k]=array[t][k]-dsum[k]
    return array

def eigenvector(U,n):
    d=len(U)
    print "len of U is %d"%d
    eigv_tem=[]
    eigv=[]
    for i in range(n):
        for j in range(d):
            eigv_tem.append(U[j][i])
        eigv.append(eigv_tem)
        eigv_tem=[]
    return eigv

def eigenvalue(array,eigenvector):
    x=[]
    y=[]
    for i in range(len(array)):
        x_tem=np.inner(eigenvector[0],array[i])
        y_tem=np.inner(eigenvector[1],array[i])
        x.append(x_tem)
        y.append(y_tem)
    return x,y

digital_array=readdigital(3)
sample_num=len(digital_array)
print sample_num
digital_array=mean(digital_array)
digital_mat=np.matrix(digital_array)
Cmat=(digital_mat.T*digital_mat)


U,s,VT=np.linalg.svd(Cmat)
U_array=np.array(U)
eigenvector=eigenvector(U_array,2)

x,y=eigenvalue(digital_array,eigenvector)

print len(x)
print len(y)
plot(x,y,'o')
show()










