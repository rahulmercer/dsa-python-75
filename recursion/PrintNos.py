class Solution:    
    #Complete this function
    def printNos(self,n):
        #Your code here
        if n>0:
            self.printNos(n-1)
            print(n,end=' ')
ob=Solution()
ob.printNos(10) #Prints 1 2 3 4 5 6 7 8 9 10
# Expected Time Complexity: O(N)