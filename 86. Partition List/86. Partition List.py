# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        smallHead = ListNode()
        bigHead = ListNode()
        
        temp = head
        small_ptr = smallHead
        big_ptr = bigHead

        while(temp):
            if(temp.val<x):
                small_ptr.next = temp
                small_ptr=small_ptr.next
            else:
                big_ptr.next = temp
                big_ptr=big_ptr.next

            temp=temp.next
        big_ptr.next=None
        small_ptr.next=bigHead.next    

        return smallHead.next
