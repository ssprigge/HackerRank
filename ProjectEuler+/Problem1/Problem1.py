#!/bin/python3

import math
import os
import random
import re
import sys
from decimal import Decimal


if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        if (n%3==0):
            m3=int(n/3)-1
        else:
            m3=int(n/3)
        s3=(3*(m3*(m3+1)))
        
        if (n%5==0):
            m5=int(n/5)-1
        else:
            m5=int(n/5)
        s5=(5*(m5*(m5+1)))
        
        if (n%15==0):
            m15=int(n/15)-1
        else:
            m15=int(n/15)
        s15=(15*(m15*(m15+1)))
        
        print(Decimal(s3+s5-s15)/2)
