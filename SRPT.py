#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:38:55 2020

@author: Manting
"""
def heap_insert(arr, n, x):
    j = n - 1
    parent = (j - 1) // 2
    while parent >= 0:
        if x[0] < arr[parent][0]:
            arr[j] = arr[parent]
            j = parent
            if parent == 0:
                break
            parent = (parent - 1) // 2
        else:
            break
    arr[j] = x
    
def heapify(arr, n):
    x = arr[n - 1]
    i = 0
    j = 2 * i + 1
    while j < n:
        if j + 1 < n:
            if arr[j][0] > arr[j + 1][0]:
                j += 1
        if arr[j][0] >= x[0]:
            break
        else:
            arr[(j - 1) // 2] = arr[j]
            j = 2 * j + 1
    arr[(j - 1) // 2] = x
    arr.pop(n - 1)
   
#%%
def srptHeap(proc):
    print(proc)
    start_time = time.time() # run time
    t = 0 # current arrive time
    complete = 0 # already number of finished process
    srpt = [] # heap
    total = 0 # the objective value
    
    while complete != k[j]: # until all processes finished
        for i in range(1, k[j] + 1):
            if proc[i][1] == t: # processes arrived
                srpt.append(proc[i]) 
                print(srpt)
                heap_insert(srpt, len(srpt), proc[i])
        
        if len(srpt) != 0 and srpt[0][0] == 0: # heapify
            heapify(srpt, len(srpt))
            complete += 1
            total += t
                
        if len(srpt) != 0: # reduce remaining time
            srpt[0][0] -= 1
            
        t += 1
    print("for the first k = %s jobs " % k[j])
    print("total movement :", t - 1) 
    print("the objective value:", total) 
    print("run time: %s seconds" % (time.time() - start_time),'\n')

#%% main
import time
import pandas as pd
k = [5]
for j in range(len(k)):
    df = (pd.read_excel("test instance.xlsx",header = None)).transpose() # read excel
    proc = df.values.tolist() # transform to list
    srptHeap(proc)
