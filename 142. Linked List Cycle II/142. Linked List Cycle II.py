# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_ptr = head
        fast_ptr = head

        if(not fast_ptr or not fast_ptr.next):
            return None

        while(fast_ptr and fast_ptr.next):
            slow_ptr=slow_ptr.next
            fast_ptr = fast_ptr.next.next
            
            if(fast_ptr==slow_ptr):
                break

        if(fast_ptr==slow_ptr):
            slow_ptr=head
            while(slow_ptr != fast_ptr):
                slow_ptr=slow_ptr.next
                fast_ptr = fast_ptr.next

            return slow_ptr
        else:
            return None
