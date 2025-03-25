def findGCD(a,b):
    while b:
        a,b = b,a%b
    return a
print(findGCD(10,15)) #Prints 5
print(findGCD(14,28)) #Prints 14
print(findGCD(3,9)) #Prints 3