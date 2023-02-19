# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head or not head.next):
            return head

        odd_dummy = ListNode(0,head)
        even_dummy = ListNode(0,head.next)
        odd_ptr=odd_dummy.next
        even_ptr=even_dummy.next
        count=3
        curr_node = head.next.next
        while(curr_node):
            if(count%2!=0):
                odd_ptr.next=curr_node
                odd_ptr=odd_ptr.next
            else:
                even_ptr.next=curr_node
                even_ptr=even_ptr.next
 
            curr_node = curr_node.next
            count+=1
        even_ptr.next=None
        odd_ptr.next=even_dummy.next


        return head
