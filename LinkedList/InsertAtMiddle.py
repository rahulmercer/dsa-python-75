class Solution:
    def insertInMiddle(self, head, x):
        #code here
        if head==None:
            return Node(x)
        fast=head.next
        slow=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        temp=Node(x)
        temp.next=slow.next
        slow.next=temp
        return head
    
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None