# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1 = self.get_num(l1)
        num2 = self.get_num(l2)
        result = num1+num2

        return self.create_linked_list(str(result))

    def create_linked_list(self,s):

        index=0
        dummy = ListNode()
        curr=dummy
        while(index<len(s)):
            curr.next = ListNode(int(s[index]))
            curr = curr.next
            index+=1

        return dummy.next

    def get_num(self,ll):
        num = ''
        while(ll):
            num+=str(ll.val)
            ll=ll.next

        return int(num)
