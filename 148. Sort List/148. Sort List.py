# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(head == None or head.next ==None):
            return head

        # finding middle of a linked-list
        slow_ptr = head
        fast_ptr = head
        prev = None

        while(fast_ptr!=None and fast_ptr.next !=None):
            prev=slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        prev.next = None
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(slow_ptr)

        return self.merge(left_sorted,right_sorted)
        
    def merge(self,head1,head2):
        
        dummy = ListNode()
        curr = dummy
        while(head1!=None and head2!=None):
            if(head1.val >= head2.val):
                curr.next = head2
                head2 = head2.next
            else:
                curr.next = head1
                head1 = head1.next
            curr = curr.next
            
        if(head1!=None):
            curr.next = head1

        if(head2!=None):
            curr.next = head2

        return dummy.next
