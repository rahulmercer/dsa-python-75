def BinarySearch(arr,key):
    left=0
    right=len(arr)-1
    while left<=right:
        mid = (left + right) // 2
        if arr[mid]>key:
            right=mid-1
        elif arr[mid]<key:
            left=mid+1
        else:
            return True
    return False

arr=[1,2,3,4,5]
key=2
result=BinarySearch(arr,key)
print("Key found!") if result==True else print("Key is not present!!!")
arr1=[1,2,3,4,50,55,60]
key1=55
result=BinarySearch(arr1,key1)
print("Key found!") if result==True else print("Key is not present!!!")