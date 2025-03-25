def isPalindrome(n):
    return str(n) == str(n)[::-1]


print(isPalindrome(1233321)) #Prints True
print(isPalindrome(121221)) #Prints False