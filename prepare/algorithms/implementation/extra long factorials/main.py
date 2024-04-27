#!/bin/python3
# https://www.hackerrank.com/challenges/extra-long-factorials/

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n<2:return n
    return n*extraLongFactorials(n-1)

if __name__ == '__main__':
    n = int(input())

    print(extraLongFactorials(n))
