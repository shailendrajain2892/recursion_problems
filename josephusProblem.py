import sys


def josephus(n, k):
    if n ==1 : 
        return 0
    return (josephus(n-1,k)+k)%n 

n = int(sys.argv[1])
k = int(sys.argv[2])
print(
    josephus(n, k)+1)