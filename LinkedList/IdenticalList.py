class Solution:
    #Function to check whether two linked lists are identical or not.
    def areIdentical(self, head1, head2):
        # Code here
        while head1 and head2:
            if head1.data!=head2.data:
                return False
            head1=head1.next
            head2=head2.next
        if head1!=None:
            return False
        if head2!=None:
            return False
        return True