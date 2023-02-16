# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if(left==right): return head

        count = 1
        left_ptr=None
        curr=head
        prev=None
        str_ptr=None
        while(count<=right):
            if(count==left-1):
                left_ptr=curr
                curr=curr.next
            elif(count==left):
                prev=curr
                str_ptr=curr
                curr=curr.next
            elif(count>left):
                if(left_ptr and count==right):
                    left_ptr.next=curr

                temp = curr.next
                curr.next=prev
                prev=curr
                curr=temp
            else:
                curr=curr.next

            count+=1

        str_ptr.next=curr

        return head if left>1 else prev
