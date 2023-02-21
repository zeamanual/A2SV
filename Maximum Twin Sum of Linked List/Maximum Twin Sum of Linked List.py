# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        temp = head
        size = 0
        # getting size of the linked list
        while(temp):
            size+=1
            temp = temp.next

        temp = head
        prev=None
        half=None
        # getting the half node
        for i in range(size):
            if(i==(size/2)):
                half=temp
                break
            temp = temp.next   
        curr = half
        prev=None
        # reversing starting from half
        while(curr):
            real_next = curr.next
            curr.next = prev
            prev= curr
            curr=real_next
        ptr_one = head
        ptr_two = prev
        max_sum =0
        # 
        for i in range(size//2):
            max_sum = max(max_sum,(ptr_one.val+ptr_two.val))
            ptr_one=ptr_one.next
            ptr_two = ptr_two.next


        return max_sum
