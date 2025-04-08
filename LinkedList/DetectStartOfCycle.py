class Solution:
    def detectStartOfCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mp = set()
        while head is not None:
            if head in mp:
                return head
            mp.add(head)
            head = head.next
        return None