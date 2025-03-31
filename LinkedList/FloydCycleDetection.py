def FloydCycleDetection(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    if not fast or not fast.next:
        return False
    slow=head
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    return slow
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def printList(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = head.next # Creating a cycle
check = FloydCycleDetection(head)
if check:
    print("Cycle detected at node with value:", check.data)
else:
    print("No cycle detected")