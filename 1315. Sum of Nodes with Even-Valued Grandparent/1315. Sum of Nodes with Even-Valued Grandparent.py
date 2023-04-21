# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        que = deque()

        curr_sum = 0
        def dfs(node,que):
            if(node == None):
                return 
            
            nonlocal curr_sum
            if(len(que)>1):
                if(que[0]%2==0):
                    curr_sum+=node.val

                que.popleft()
            que.append(node.val)
            dfs(node.left,que.copy())
            dfs(node.right,que.copy())
                  
        dfs(root,que)
        return curr_sum
