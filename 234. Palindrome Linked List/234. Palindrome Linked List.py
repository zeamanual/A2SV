# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        stack = []

        temp = head 
        linkedList_size=0
        while(temp):
            stack.append(temp)
            linkedList_size+=1
            temp=temp.next

        curr=head
        for i in range(linkedList_size//2):
            cors_value = stack.pop().val
            if(curr.val!=cors_value):
                return False
            curr=curr.next

        return True
