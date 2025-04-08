class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        #Your code here
        mp = set()
        while head is not None:
            if head in mp:
                break
            mp.add(head)
            head = head.next
        headloop=head
        count=0
        while head is not None:
            head=head.next
            count+=1
            if head==headloop:
                break
        return count