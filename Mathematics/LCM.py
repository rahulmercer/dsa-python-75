def findGCD(a,b):
    while b:
        a,b = b,a%b
    return a



def LCM(a,b):
    return a*b//findGCD(a,b)
print(LCM(10,15)) #Prints 30
print(LCM(14,28)) #Prints 28
print(LCM(3,9)) #Prints 9

