def findSequenceSum(n):
    if n==0:
        return 0
    return n+findSequenceSum(n-1)
n=5
print(findSequenceSum(n)) #Prints 15