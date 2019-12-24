import math
import os
import random
import re
import sys
from collections import defaultdict
import numpy as np

def rotate90Clockwise(a,x1, y1, x2, y2):
  b=a[x1:x2,y1:y2]
  b=np.rot90(b, k=1, axes=(1,0))
  k=0;
  for i in range(x1,x2):
    l=0
    for j in range(y1,y2):
      a[i][j]=b[k][l]
      l+=1
    k+=1
  return(a)

# Function to print the matrix
def printMatrix (M):
    print(np.matrix(M))
# Complete the quickSort function below.
def kingRichardKnights(n, s, commands, knights):

  a=np.arange(n*n)
  a= a.reshape(n,n)
  printMatrix(a)



  for i in range (0, len(commands)):
    x1= commands[i][0]-1
    y1 = commands[i][1]-1
    x2= x1+commands[i][2]
    y2 = y1+commands[i][2]
    a= rotate90Clockwise(a, x1,y1 ,x2,y2 )

  printMatrix(a)






if __name__ == '__main__':
    n = 7

    s = 4

    commands = [[1, 2, 4], [2, 3, 3], [3, 4, 1], [3, 4, 0]]
    knights = []



    result = kingRichardKnights(n, s, commands, knights)
