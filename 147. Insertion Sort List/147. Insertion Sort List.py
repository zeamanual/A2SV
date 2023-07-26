# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(not head or not head.next):
            return head

        sorted_head = ListNode(0,head)
        sorted_tail = head

        curr = head.next
        while(curr):
            if(curr.val >= sorted_tail.val):
                sorted_tail = curr
                curr=curr.next
            else:
                sorted_tail.next = curr.next
             
                pos_ptr = sorted_head
                while(pos_ptr.next.val<curr.val):
                    prev=pos_ptr
                    pos_ptr = pos_ptr.next
                
                curr.next = pos_ptr.next
                pos_ptr.next =curr

                curr=sorted_tail.next

        return sorted_head.next
