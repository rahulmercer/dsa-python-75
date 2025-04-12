def removeDuplicates(head):
    #code here
    temp=head
    if head.next==None:
        return head
    while temp:
        while temp.next and temp.data==temp.next.data:
            temp.next=temp.next.next
        temp=temp.next
    return head
