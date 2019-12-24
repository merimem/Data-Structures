# Python code to demonstrate naive
# method to compute gcd ( recursion )

def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

# Approach 2
# Python code to demonstrate naive
# method to compute gcd ( Loops )


def computeGCD(x, y):

    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd 
