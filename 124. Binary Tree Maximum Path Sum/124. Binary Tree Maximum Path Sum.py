# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum= float('-inf')
        
        def dfs(node):
           
            nonlocal max_sum
            if(node==None):
                return 0
  
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            max_sum = max(max_sum,node.val,node.val+left_sum,node.val+right_sum,left_sum+right_sum+node.val)

            return max(node.val,node.val+left_sum,node.val+right_sum)

        dfs(root)
        return max_sum
