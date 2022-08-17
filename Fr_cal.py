# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:12:52 2022

@author: Lenovo
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

 ：： 处理径向力计算函数

This is a temporary script file.
"""
import os
import pandas as pd
import math
# import matplotlib.pyplot as plt
# import constants as cst
# import numpy as np


# 坐标系判断函数
def coorSysJudege(x,y):
    if x>=0 and y >=0:       # 第一象限
        ax = [1,1]
    elif x>=0 and y <=0:     # 第四象限
        ax = [1,-1]
    elif x<= 0 and y>= 0:    # 第二象限
        ax = [-1,1]
    elif x<=0 and y <=0:     # 第三象限
        ax =[-1,-1]
    else:
        ax = [0,0]
    return ax
        
def calTheta(x,y,ax):
    fm = math.sqrt(x*x + y*y)
    if(ax == [1,1]):                                                       # 第一象限
        theta = math.asin(abs(y)/fm )
        theta2 = theta
    elif (ax == [-1,-1]):                                                  # 第三象限
        theta = math.asin(abs(y)/fm ) 
        theta2 = theta + math.pi
    elif (ax == [-1,1]):
        theta = math.asin(abs(x)/fm )   
        theta2 = theta + math.pi*0.5
                
    elif (ax == [1,-1]):
        theta = math.asin(abs(x)/fm )
        theta2 = theta + math.pi*1.5
        
    else:
        theta = 0
        theta2 =0
    return [theta,theta2]
        
def cal_F_ridal(theta,fx,fy,ax):
    if ax==[1,1]:
        Fr = fx*math.cos(theta) + fy*math.sin(theta)
        theta2 = theta
    elif ax == [-1,-1]:
        Fr = -1*fx*math.cos(theta)  - fy*math.sin(theta)
        theta2 = theta + math.pi
    elif ax == [-1,1]:
        Fr = -fx*math.sin(theta) + fy*math.cos(theta)
        theta2 = theta + math.pi*0.5
    elif ax == [1,-1]:
        Fr = fx*math.sin(theta) - fy*math.cos(theta) 
        theta2 = theta + math.pi*1.5
    else:
        Fr = 0 
    return [theta2/math.pi*180,Fr]
    
def merge01(l,m):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] ==l[j]:
                m[i]= m[i] + m[j];
                m[j] = 0
                l[j] = 0     
    return [l,m]

def deldup(a):

    for i in range(len(a)-1,0,-1):
        if a[i]==0:
            del a[i]        
    return a

path = r"D:\03-work\tem\radial_force3000.csv"

df = pd.read_csv(path,header=0) 
x =  df.iloc[1:,0].tolist(); 
y =  df.iloc[1:,1].tolist();
fx = df.iloc[1:,2].tolist();
fy = df.iloc[1:,3].tolist();


# print(len(x))
# print(len(y))

# print(len(fx))
# print(len(fy))
di = [[1,1],[-1,1],[-1,-1],[1,-1]]
xiax = 0;


# 定义2个列表存储  角度和径向力
L_theta = []
L_Fr  =[]
if(len(x) == len(y) and len(x)==len(fx) and len(fx) == len(fy)):
    
    for i in range(len(x)):
        ax = coorSysJudege(x[i], y[i])
        # 计算sqrt(x^2 + y^2) ,计算sin角度
        theta = calTheta(x[i], y[i], ax)
        # print(theta[1]/math.pi*180)
        # print(ax)
        ret = cal_F_ridal(theta[0],fx[i],fy[i],ax)
        L_theta.append(round(ret[0],1))
        L_Fr.append(ret[1])
QF = merge01(L_theta, L_Fr)        
a = deldup(QF[0])
b = deldup(QF[1])

# fig = plt.figure(figsize=(5, 5))        
        
# ax1 = plt.gca(projection='polar') 
# ax1.set_thetagrids(np.arange(0.0, 360.0, 15.0), fontproperties=cst.FONT_LEGEND_EN) 
# ax1.set_thetamin(0.0)  # 设置极坐标图开始角度为0° 
# ax1.set_thetamax(180.0)  # 设置极坐标结束角度为180°   
# ax.set_rgrids(np.arange(0, 5000.0, 1000.0))      

            
        