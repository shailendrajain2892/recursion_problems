import sys


def sumOfN(n):
    if n==0:
        return 0
    return n+sumOfN(n-1)

print(sumOfN(int(sys.argv[1])))