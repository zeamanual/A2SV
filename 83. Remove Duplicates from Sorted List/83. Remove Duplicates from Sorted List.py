# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        if( not head or  not head.next):
            return head

        dummy = ListNode(0,head)
        left_ptr = head
        right_ptr=head.next

        while(right_ptr):
            if(left_ptr.val==right_ptr.val):
                right_ptr=right_ptr.next
            else:
                left_ptr.next=right_ptr
                left_ptr=left_ptr.next
                right_ptr=right_ptr.next
        
        left_ptr.next=None

        return head

