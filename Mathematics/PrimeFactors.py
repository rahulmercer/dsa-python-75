def FindPrimeFactor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
print(FindPrimeFactor(10)) #Prints 5
print(FindPrimeFactor(15)) #Prints 5
print(FindPrimeFactor(13)) #Prints 13