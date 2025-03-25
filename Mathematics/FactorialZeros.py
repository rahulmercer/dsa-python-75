def CountZeros(n:int)->int:
    count = 0
    i = 5
    while n / i >= 1:
        count += int(n / i)
        i *= 5
    return count

print(CountZeros(100)) #Prints 24
print(CountZeros(1000)) #Prints 249
print(CountZeros(10)) #Prints 2