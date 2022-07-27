#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    new_num = arr[n-1]
    isFinished=False
    for i in range(n-2,-1,-1):
        if(new_num<arr[i]):
            arr[i+1]=arr[i]  
        else:
            arr[i+1]=new_num
            isFinished=True
        for num in arr:
            print(num,end=' ')
        print('')
        if(isFinished):
            break

    if(not isFinished):
        arr[0]=new_num
        for num in arr:
            print(num,end=' ')

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
