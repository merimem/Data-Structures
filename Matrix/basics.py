import math
import os
import random
import re
import sys
from collections import defaultdict
import numpy as np

def printMatrix (M, n):
    print(np.matrix(M))
# Complete the quickSort function below.
def kingRichardKnights(n, s):

  a=np.arange(n*n)
  a= a.reshape(n,n)
  printMatrix(a, n)






if __name__ == '__main__':
     n = int(input())

    s = int(input())

    commands = []
    knights = []

    for _ in range(s):
        commands.append(list(map(int, input().rstrip().split())))
    for _ in range(s):
        knights.append(list(map(int, input().rstrip().split())))

    #result = kingRichardKnights(n, s, commands, knights)
    kingRichardKnights(7, 4)
