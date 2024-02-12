import sys


def subsetSum(nl, n, sum):
    if n == 0:
        return 1 if sum == 0 else 0
    return subsetSum(nl, n-1, sum) + subsetSum(nl, n-1, sum-nl[n-1])


lst1 = [int(item) for item in input("Enter the list items : ").split()]
sum = input("Enter expected Sum for a given set:")
print(subsetSum(lst1, len(lst1), int(sum)))