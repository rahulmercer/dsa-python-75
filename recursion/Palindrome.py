class Solution:
    def isPalin(self,N):
        def check(s,left,right):
            if left>=right:
                return True
            if s[left]!=s[right]:
                return False
            return check(s,left+1,right-1)
        s=str(N)
        return check(s,0,len(s)-1)
ob=Solution()
print(ob.isPalin(121)) #Prints True
print(ob.isPalin(1212)) #Prints False
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(N) for recursive stack