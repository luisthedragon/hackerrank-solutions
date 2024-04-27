#!/bin/python3
# https://www.hackerrank.com/challenges/compare-the-triplets/problem

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    ar=[0,0]
    for i in range(a.__len__()):
        if a[i]>b[i]:
            ar[0]+=1
        elif a[i]<b[i]:
            ar[1]+=1
    return ar
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
