# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:58:02 2022

@author: User
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize
import random as rd
#%%

counts = pd.read_excel('courseid_40977_participants.xlsx',usecols=['姓名','學號','上台次數'])
counts.iloc[:,1] = counts.iloc[:,1].astype(str)
ID = counts.iloc[:,0:2]
#%% reset 上台次數 to 0
counts.iloc[:,2] = np.zeros(30)

#%% check 抽到重複的人
def check(draw):
    for j in range(len(draw)):
        if(draw[len(draw)-1]==draw[j]):
            draw[len(draw)-1] = rd.randrange(30)
            check(draw)
        else:
            break
    
    return draw
#%%
flag = 0
i = 0
draw = [-1] 
num = 5 #抽幾個人
while(1):
    if(flag>= num):
        break
    draw[i] = rd.randrange(30)
    if(flag>0):
        draw = check(draw)
    if(counts.iloc[draw[i],2]-np.mean(counts.iloc[:,2])>0.01):
        pass
    else:    
        counts.iloc[draw[i],2] = counts.iloc[draw[i],2] + 1
        print(i+1,ID.iloc[draw[i],1],ID.iloc[draw[i],0])
        i = i + 1
        flag = flag + 1
        draw = draw + [-1] if flag<num else draw
#%%
#print(counts)