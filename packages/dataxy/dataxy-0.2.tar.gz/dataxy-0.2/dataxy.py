#!/usr/bin/env python
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[4]:


def dataxy(data,window_size=1800,look_back=300,step_size=300,jg=10):
    # 创建一个n行n列的二维列表，每个元素都设置为300
    lok=pd.DataFrame([[look_back] *index1.shape[0]] * 1,columns=index1)
    kk=[180,120,120,60,60,60,60,60,60,60,60,120,120,120,1800,1200,600,600]
    lok[de]=kk 
    k=np.shape(data)[0]##172800
    m=np.shape(data)[1]#25
    X, y = [], []
    x_data=data.values
    y_data=data['V4::DPU1001.SH0161.AALM1.PV'].values
    for i in range(k-window_size-step_size+1):#行
        a=np.array([[]], dtype=int)
        for j in range(m):#25
            start=i+window_size-lok.iloc[0,j]
            b=x_data[range(start,(start+min(lok.iloc[0,j],look_back)),jg),j].reshape(1,-1)
            a = np.concatenate((a, b),axis=1)
        X.append(a[0])
        y.append(y_data[i+window_size:i+window_size+step_size])
    return pd.DataFrame(X),pd.DataFrame(data=y)


# In[ ]:




