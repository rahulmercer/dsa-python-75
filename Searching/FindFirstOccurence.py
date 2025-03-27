def FirstOccurence(arr,key):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2

        if key>arr[mid]:
            left = mid + 1
        elif key<arr[mid]:
            right=mid-1
        else:
            if mid==0 or arr[mid-1]!=arr[mid]:
                return mid
            else:
                right=mid-1
    return -1



arr=[1,2,3,4,5]
key=2
result=FirstOccurence(arr,key)
print("Key found!") if result!=-1 else print("Key is not present!!!")
arr1=[1,2,3,4,50,55,60]
key1=55
result=FirstOccurence(arr1,key1)
print("Key found!") if result!=-1 else print("Key is not present!!!")