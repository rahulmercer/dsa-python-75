# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        hare=head
        tortoise=head
        while hare and hare.next and tortoise:
            hare=hare.next.next
            tortoise=tortoise.next
        return tortoise
