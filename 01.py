import math
import numpy as np
import random
import scipy.stats as ss
from pylab import *



def sample_y_fun(sample_num):
    sample_list=[]
    part=1.0/(sample_num-1)
    for i in range(sample_num):
        append_num=np.sin(i*part*2*pi)+np.random.normal(0,1)/5
        sample_list.append(append_num)
        print sample_list[i]
    return sample_list

def draw_sin():
    x=np.linspace(0,1,256,endpoint=True)
    y=np.sin(np.pi*x*2)
    xticks([0,1])
    yticks([-1,0,1])
    plot(x,y)


def sample_x_fun(sample_num):
    x=[]
    for i in range(sample_num):
        x.append(float(i)/float(sample_num-1))
    return x


def reg(x,y,degree):
    x_arr=[]
    sam_num=len(x)
    for i in range(sam_num):
        x_tem_arr=[]
        for j in range(degree+1):
            x_tem=x[i]**(degree-j)
            x_tem_arr.append(x_tem)
        x_arr.append(x_tem_arr)
    x_mat=mat(x_arr)
    y_mat=mat(y).T
    xTx=x_mat.T*x_mat
    pl=(xTx.I)*(x_mat.T*y_mat)
    return pl

def reg_numda(x,y,degree,numda):
    x_arr=[]
    sam_num=len(x)
    for i in range(sam_num):
        x_tem_arr=[]
        for j in range(degree+1):
            x_tem=x[i]**(degree-j)
            x_tem_arr.append(x_tem)
        x_arr.append(x_tem_arr)
    x_mat=mat(x_arr)
    y_mat=mat(y).T
    xTx=x_mat.T*x_mat
    n=len(xTx)
    I=np.identity(n)
    pl=(xTx.I-numda*I)*(x_mat.T*y_mat)
    return pl

def draw_reg(pl):
    xx=np.linspace(0,1,256)
    plot(xx,polyval(pl,xx),'r-')

def draw_sample(x,y):
    plot(x,y,'o')


def reg_result(degree,sample_num):
    draw_sin()
    x=sample_x_fun(sample_num)
    y=sample_y_fun(sample_num)
    draw_sample(x,y)
    pl=reg(x,y,degree)
    draw_reg(pl)
    show()


def reg_result_numda(degree,sample_num,lnnumda):
    draw_sin()
    x=sample_x_fun(sample_num)
    y=sample_y_fun(sample_num)
    draw_sample(x,y)
    numda=2.718**(lnnumda)
    pl=reg_numda(x,y,degree,numda)
    draw_reg(pl)
    show()


reg_result(3,10)
reg_result(9,10)
reg_result(9,15)
reg_result(9,100)
reg_result_numda(9,10,-2)
reg_result_numda(9,15,-18)








        
        
