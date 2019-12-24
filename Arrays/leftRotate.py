

def leftRotatebyOne(T, n):
    temp = T[0]
    for i in range(n-1):
        print(T[i],"+", T[i+1])
        T[i]=T[i+1]
    T[n-1] = temp
    print(T)

def leftRotate(T,d, n):
    for i in range(d):
        leftRotatebyOne(T, n)

def printArray(T, n):
    for i in range(n):
        print(T[i])

T = [1, 2, 3, 4, 5, 6, 7]
n = len(T)
print(n)
print(T)
d = 2
leftRotate(T, d, n)
#printArray(T, n)
print(T)
