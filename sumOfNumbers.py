import sys


def sumOfNumbers(N):
    if N==0:
        return 0
    return N%10+sumOfNumbers(N//10)

print(sumOfNumbers(int(sys.argv[1])))