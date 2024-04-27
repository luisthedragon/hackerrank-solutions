#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, N):
    raiz=int(math.pow(X,1.0/N))
    n=0
    acum=0
    cont=0
    s=[]
    v=[]
    for i in range(raiz):
      s.append(-1)  
      v.append((i+1)**N)
    
    while(n>=0):
       # print(s,acum)
        s[n]+=1
        if s[n]==1:
            acum+=v[n]
        
        if(acum==X):
            cont+=1
        
        if(acum<X and n<raiz-1):
            n+=1
        else:
            while(s[n]==1 and n>=0):
                acum-=v[n]
                s[n]=-1
                n-=1
                

    return cont



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
