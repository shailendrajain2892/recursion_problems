import sys

def towerOfHanoi(N, fromm, to, aux):
    # if N == 1:
    #     print(f"move disk 1 from rod {fromm} to rod {to}")
    #     count.append(1)
    #     return
    if N == 0:
        return 0
    
    moves = towerOfHanoi(N-1, fromm, aux, to)
    print(f"move disk {N} from rod {fromm} to rod {to}")
    moves += 1
    moves += towerOfHanoi(N-1, aux, to, fromm)
    return moves

print(towerOfHanoi(int(sys.argv[1]), 1, 3, 2))

