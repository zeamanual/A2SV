# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if(not head):
            return None

        size = 0
        temp = head
        prev=None
        while(temp):
            size+=1
            prev=temp
            temp = temp.next
        prev.next = head

        k = k%size
        temp = ListNode(0,head)
        itr_count=0
        while(itr_count<(size-k)):
            temp=temp.next
            itr_count+=1
        head = temp.next
        temp.next=None
        
        return head
