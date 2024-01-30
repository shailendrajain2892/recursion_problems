import sys

# time complexity O(3^n)
def cutTheRope(N, a, b, c):
    if N==0:
        return 0
    elif N<0:
        return -1
    res = max(
        cutTheRope(N-a, a, b, c), 
        cutTheRope(N-b, a, b, c),
        cutTheRope(N-c, a, b, c)
        )
    if res == -1:
        return -1
    return res+1

N = int(sys.argv[1])
a = int(sys.argv[2])
b = int(sys.argv[3])
c = int(sys.argv[4])
print(cutTheRope(N, a, b, c))