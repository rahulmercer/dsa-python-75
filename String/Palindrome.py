def PalindromeArray(arr):
    for i in range(len(arr)):
        if arr[i]==arr[len(arr)-1-i]:
            continue
        else:
            return False
    return True
def PalindromeString(str):
    return str==str[::-1]
def PalindromeString2(str):
    left=0
    right=len(str)-1
    while left<=right:
        if str[left]!=str[right]:
            return False
        left+=1
        right-=1
    return True

Str="madam"
Str1="hello"
Str2="abcba"
print("String is Palindrome") if PalindromeString(Str) else print("String is not Palindrome")
print("String is Palindrome") if PalindromeString(Str1) else print("String is not Palindrome")
print("String is Palindrome") if PalindromeString(Str2) else print("String is not Palindrome")
