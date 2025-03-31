# Efficient solution
# Time Complexity: O(nlogn)
def Anagram(str1, str2):
    if len(str1)!=len(str2):
        return False
    str1=sorted(str1)
    str2=sorted(str2)
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            return False
    return True
# Naive solution
# Time Complexity: O(n^2)
def Anagram2(str1, str2):
    if len(str1)!=len(str2):
        return False
    count=[0]*256
    for i in range(len(str1)):
        count[ord(str1[i])]+=1
        count[ord(str2[i])]-=1
    for i in range(len(count)):
        if count[i]!=0:
            return False
    return True
    
# Driver code
Str1="listen"
Str2="silent"
Str3="hello"
Str4="world"
print("Anagram") if Anagram(Str1, Str2) else print("Not Anagram")
print("Anagram") if Anagram(Str3, Str4) else print("Not Anagram")
print("\n")
print("Anagram") if Anagram2(Str1, Str2) else print("Not Anagram")
print("Anagram") if Anagram2(Str3, Str4) else print("Not Anagram")
