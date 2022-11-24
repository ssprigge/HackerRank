#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input().strip())
    f=[1,1,2,3,5,8]
    e=[2,8]
    i=5
    
    while i < 80:
        f.append(f[i]+f[i-1])
        if (f[i]+f[i-1])%2 == 0:
            e.append(f[i]+f[i-1])
        i=i+1
        
    for t_itr in range(t):
        n = int(input().strip())
        print(sum(list(filter(lambda x : x<=n, e))))

