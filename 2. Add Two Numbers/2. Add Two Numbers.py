# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_num = ''
        second_num = ''

        while(l1):
            first_num= str(l1.val)  + first_num
            l1=l1.next
        while(l2):
            second_num= str(l2.val)  + second_num
            l2=l2.next
        result = str(int(first_num)+int(second_num))

        prev=None
        last=None
        for char in result:
            last = new_node=ListNode(int(char))
            new_node.next = prev
            prev=new_node
        return last
