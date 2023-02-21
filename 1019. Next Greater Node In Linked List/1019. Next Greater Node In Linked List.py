# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        res = []

        curr = head
        size =0
        while(curr):
            res.append(None)
            if(len(stack)==0 or  curr.val <= stack[len(stack)-1][0]):
                stack.append([curr.val,size])
            else:
                last = stack[len(stack)-1]
                while (last and last[0]< curr.val):
                    res[last[1]]=curr.val
                    stack.pop()
                    last = stack[len(stack)-1] if (len(stack)>0) else None
                stack.append([curr.val,size])
            size+=1
            curr=curr.next

        for i in range(size):
            res[i]=0 if (res[i]==None) else res[i]

        return res
