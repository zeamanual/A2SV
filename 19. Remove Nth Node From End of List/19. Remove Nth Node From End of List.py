# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        dummy = ListNode(0,head)
        left_ptr = dummy
        right_ptr= head
        count = 0

        while(right_ptr!=None):
            if(count<n):
                right_ptr=right_ptr.next
            else:
                right_ptr=right_ptr.next
                left_ptr=left_ptr.next
            
            count+=1

        left_ptr.next=left_ptr.next.next

        return dummy.next
