def ReverseLinkedList(head):
    prev = None
    current = head
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move to the next node
    return prev  # New head of the reversed list

# driver code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
    def printList(self):
        current = self
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.printList()
reversed_head = ReverseLinkedList(head)
reversed_head.printList()
# Output:
# 1 -> 2 -> 3 -> 4 -> 5 -> None
# 5 -> 4 -> 3 -> 2 -> 1 -> None
# Time Complexity: O(n)
# Space Complexity: O(1)
