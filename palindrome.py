def palindrome(s, n):
    if n==0:
        return s[0]
    return s[n]+palindrome(s, n-1)


def isPalindrom(s, start, end):
    if start>=end:
        return True 
    
    return (s[start] == s[end]) and isPalindrom(s, start+1, end-1)


def main():
    pal = input("string to check palindrome:")
    if isPalindrom(pal, 0, len(pal)-1):
        print("True")
    else:
        print("False")
    # updated_pal = palindrome(pal, len(pal)-1)
    # if pal == updated_pal:
    #     print("yes pal")
    # else: 
    #     print("No Pal")

main()
