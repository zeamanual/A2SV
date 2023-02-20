# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        left_ptr = dummy
        right_ptr = head

        while(right_ptr and right_ptr.next):
            if(right_ptr.val != right_ptr.next.val):
                left_ptr.next=right_ptr
                left_ptr=left_ptr.next
                right_ptr = right_ptr.next
            else:
                temp = right_ptr.val
                while(right_ptr  and right_ptr.val == temp):
                    right_ptr=right_ptr.next

        left_ptr.next=right_ptr

        return dummy.next
