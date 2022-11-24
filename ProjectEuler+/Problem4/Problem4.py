#!/bin/python3

import math
import os
import random
import re
import sys

def ispal(x):
    p=list(str(x))
    l=len(p)
    if l%2==0:
        for i in range(int(l/2)):
            if (p[i] not in p[l-1-i]):
                return False
            else:
                i=i+1
        return True
    else:
        for i in range(int((l-1)/2)):
            if p[i] not in p[l-1-i]:
                return False
            else:
                i=i+1
        return True
    
if __name__ == '__main__':
    t = int(input().strip())
    p=[]
    for i in range(100, 1000):
        for j in range(100, i+1):
            p.append(i*j)
    p=list(filter(lambda x : ispal(x),p))
    p.sort()
    for t_itr in range(t):
        n = int(input().strip())
        i=0
        while (p[i]<n):
            i=i+1
        print(p[i-1])

