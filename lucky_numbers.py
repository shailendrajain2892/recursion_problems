import sys


def lucky(n, c):
    print(f"calling with {n} and counter : {c}")
    if c <= n:
        if n % c == 0:
            return False
        n=n-n//c
        c+=1
        return lucky(n, c)
    else:
        return True
    
def luckyNumber(n):
    return lucky(n, 2)

n = int(sys.argv[1])
print(luckyNumber(n))