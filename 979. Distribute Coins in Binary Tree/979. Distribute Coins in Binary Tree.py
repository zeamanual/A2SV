# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        move =0
        def dfs(node):
            nonlocal move
            
            if not node:
                return 0

            net=node.val-1

            left_sub=dfs(node.left)
            right_sub=dfs(node.right)
            move+=abs(left_sub)+abs(right_sub)
            net+=left_sub+right_sub
            
            return net

        dfs(root)
        return move
