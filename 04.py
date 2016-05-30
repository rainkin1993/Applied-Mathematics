from numpy import *
from math import *
from numpy.linalg import inv
from pylab import *

def LM(x,y):
    a0=10.0
    b0=0.5
    y_init=zeros(len(x))
    for i in range(len(x)):
        y_init[i]=a0*exp(-b0*x[i])
    data_num=len(x)
    para_num=2
    iter_num=50
    namda=0.01
    update=1
    a_lm=a0
    b_lm=b0
    iter=0
    y_est=zeros(len(x))
    y_est_lm=zeros(len(x))
    H=zeros([2,2])
    J = zeros([data_num, para_num])
    d=zeros(len(x))
    while iter<iter_num:
        print iter,
        for j in range(len(x)):
            J[j][0] = exp(-b_lm * x[j])
            J[j][1] = -a_lm * x[j] * exp(-b_lm * x[j])
        for k in range(len(x)):
            y_est[k] = a_lm * exp(-b_lm * x[k])
        d = y - y_est
        H = dot(J.T, J)
        H_lm= 2*H + (namda*eye(para_num))
        g = dot(J.T,d)
        dp=dot(inv(H_lm),g)
        a_lm_est=a_lm+dp[0]
        b_lm_est=b_lm+dp[1]
        for i in range(len(x)):
            y_est_lm[i]=a_lm_est*exp(-b_lm_est*x[i])
        if y_est_lm.any()-y_est.any()>0:
            namda=namda*10
        else:
            namda=namda*0.1
            a_lm=a_lm_est
            b_lm=b_lm_est
        print a_lm,
        print b_lm

        iter=iter+1

    print 'final parameter a=%f     parameter  b=%f'%(a_lm,b_lm)

    plot(x,y,'o')
    xz = np.linspace(0,10,256,endpoint= True)
    yz = a_lm*exp(-b_lm*xz)
    plot(xz,yz)
    show()



if __name__=="__main__":
    data = [1.2,1.8,2.0,1.5,5.0,3.0,4.0,6.0,8.0]
    obs = [19.21,18.15,15.36,14.10,12.89,9.32,7.45,5.24,3.01]
    LM(data,obs)
