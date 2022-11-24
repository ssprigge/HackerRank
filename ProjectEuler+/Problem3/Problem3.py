#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        p=set()
        d=2
        while n>1:
            if (n%d==0):
                n=n/d
                p.add(d)
            elif (d**2)>n:
                print(int(n))
                p=set()
                break
            else:
                d=d+1
        if not(p==set()):
            print(list(p).pop())
        

