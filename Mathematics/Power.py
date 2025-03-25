def FindPower(x,n):
    if n==0:
        return 1
    if n%2==0:
        return FindPower(x,n//2)*FindPower(x,n//2)
    return x*FindPower(x,n//2)*FindPower(x,n//2)
print(FindPower(2,3)) #Prints 8
print(FindPower(3,4)) #Prints 81