def perm(s, i=0):
    if i == len(s)-1:
        print("".join(s), end=" ")
        return
    for j in range(i, len(s)):
        s[i], s[j] = s[j], s[i]
        perm(s, i+1)
        s[i], s[j] = s[j], s[i]
    
s = input("enter string to find all possible values for it: ")
perm(list(s))
