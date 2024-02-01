import sys


def towerOfHanoi(N, a, b, c):
    if N == 1:
        print(f"Move 1 from {a} to {c}")
        return
    towerOfHanoi(N-1, a, c, b)
    print(f"Move {N} from {a} to {c}")
    towerOfHanoi(N-1, b, a, c)

towerOfHanoi(int(sys.argv[1]), 'a', 'b', 'c')
