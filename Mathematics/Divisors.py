def FindDivisors(n):
    i=1
    while i*i<n:
        if n%i==0:
            print(i,end=" ")
        i+=1
    while i>=1:
        if n%i==0:
            print(n//i,end=" ")
        i-=1
FindDivisors(100)
FindDivisors(10)