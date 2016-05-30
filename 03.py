# coding=utf-8
import numpy as np
from scipy.stats import multivariate_normal as mvn

def generate_data(n):
    pi=np.array([0.4,0.6])
    miu=np.array([[2,4],[0,5]])
    sigma=np.array([[[2,0],[0,0.5]],[[1,0],[0,3]]])
    x=np.concatenate([np.random.multivariate_normal(m,s,int(p*n)) for m,s,p in zip(miu,sigma,pi)])
    print len(x)
    return miu,sigma,pi,x

def initialpara(k,d):
    global pi_em,miu_em,sigma_em
    pi_em=np.random.random(k)
    pi_em/=pi.sum()
    miu_em=np.random.random((k,d))
    sigma_em=np.array([np.eye(d)]*k)

def EM(x):
    global n,d,k,iter,pi_em,sigma_em,miu_em,likelihood_new
    numda=0.01
    likelihood_odd=0
    for ite in range(iter):
        #E_step:
        w=np.zeros((k,n))
        for i in range(k):
            for j in range(n):
                w[i,j]=pi_em[i]*mvn(miu_em[i],sigma_em[i]).pdf(x[j])
        w/=w.sum(0)

        #M_step
        pi_em=np.zeros(k)
        miu_em=np.zeros((k,d))
        sigma_em=np.zeros((k,d,d))
        for i in range(k):
            for j in range(n):
                pi_em[i]+=w[i,j]
                miu_em[i]+=w[i,j]*x[j]
            miu_em[i]/=pi_em[i]
        pi_em/=n

        for i in range(k):
            for j in range(n):
                tmp=np.reshape(x[j]-miu_em[i],(2,1))
                sigma_em[i]+=w[i,j]*np.dot(tmp,tmp.T)
            sigma_em[i]/=w[i,:].sum()

        likelihood_new=0
        for i in range(n):
            s=0
            for j in range(k):
                s+=pi_em[j]*mvn(miu_em[j],sigma_em[j]).pdf(x[i])
            likelihood_new+=np.log(s)

        if np.abs(likelihood_new-likelihood_odd) < numda:
            break
        likelihood_odd=likelihood_new
        print ite


n=1000 
d=2 
k=2 
iter=100
miu,sigma,pi,x=generate_data(n)
initialpara(k,d)
EM(x)

