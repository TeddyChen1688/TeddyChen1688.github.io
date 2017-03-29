# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import sqrt
def isprime(x):
    if x == 1:
        return False
    k=int(sqrt(x))
    for j in range(2,k+1):
        if x%j==0:
            return False
    return True

i=1
k=2
while(i<6):
    print ('Hello')
    while(isprime(k)):
        m=pow(k,2)-1
        if isprime(m):
            print i,k,m
            k+=1
            i+=1
        else: k+=1
  

