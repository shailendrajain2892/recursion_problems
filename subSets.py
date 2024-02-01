import sys


def subSets(s, curr, idx, sublist):
    if len(s) == idx:
        sublist.append(curr)
        return 
    subSets(s, curr, idx+1, sublist)
    subSets(s, curr+s[idx], idx+1, sublist)

def calSubset(s):
    subsetlist=[]
    subSets(s, "", 0, subsetlist)
    print(subsetlist)

calSubset("abcd")    

