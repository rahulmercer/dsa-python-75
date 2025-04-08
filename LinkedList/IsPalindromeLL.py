class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        while head is not None:
            arr.append(head.val)
            head=head.next
        length=len(arr)
        for i in range(len(arr)):
            if arr[i]!=arr[length-i-1]:
                return False
        return True