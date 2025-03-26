def rotateList(arr,d):
    n=len(arr)
    d=d%n
    temp=[]
    for i in range(d):
        temp.append(arr[i])
    for i in range(d,n):
        arr[i-d]=arr[i]
    for i in range(d):
        arr[n-d+i]=temp[i]
    return arr
# Driver code
arr = [1, 2, 3, 4, 5, 6, 7]
d=2 #Number of rotations
print(rotateList(arr,d)) #Prints [3, 4, 5, 6, 7, 1, 2]
# Time complexity: O(n)