#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(nums):
    # Write your code here
    swap_count =0
    n = len(nums)
    for i in range(n-1):
        for j in range(n-1):
            if (a[j] > a[j + 1]):
                swap_count+=1
                swap(nums,j, j + 1)
    print(f"Array is sorted in {swap_count} swaps.")
    print(f"First Element: {nums[0]}")
    print(f"Last Element: {nums[-1]}")  

   
def swap(nums,index_one,index_two):
    nums[index_one],nums[index_two]= nums[index_two],nums[index_one]    
    

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
