# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:01:52 2019

@author: New
"""

te1,te2=map(int,input().split())
li=list(map(int,input().split()))
dum=0
lo=0
while te2>0:
  te2=te2-86400+li[lo]
  dum+=1
  lo+=1
print(dum)