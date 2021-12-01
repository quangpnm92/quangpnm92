#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    calculated = 0
    stack_fwr = []
    stack_bwr = []
    for i in range(0,h,1):
        for j in range(i+1,h,1):
            if h[i] <= h[j]:
                stack_fwr.append(h[i])
            elif not (stack_fwr.empty()):
                calculated = h[i] * len(stack_fwr)

            elif (stack_bwr.empty()):
                
                 #if stack null => check behind
                #check behind


    return calculated

if __name__ == '__main__':
    abc = open('abc.txt', 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    abc.write(str(result) + '\n')

    abc.close()
