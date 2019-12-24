#!/bin/python3
#HACKERRANK
#Sorting is useful as the first step in many different tasks.
#The most common task is to make finding things easier, but there are other uses as well.
#In this case, it will make it easier to determine which pair or pairs of elements have the
# smallest absolute difference between them.
import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the closestNumbers function below.
def closestNumbers(nums):
    nums.sort()
    lowestDiff = nums[1]-nums[0]
    res = [nums[0],nums[1]]
    for i in range(1,len(nums)-1):
        if nums[i+1]-nums[i] < lowestDiff:
            res = []
            res.append(nums[i])
            res.append(nums[i+1])
            lowestDiff = abs(nums[i+1]-nums[i])
        elif nums[i+1]-nums[i] == lowestDiff:
            res.append(nums[i])
            res.append(nums[i+1])
    return(res)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
