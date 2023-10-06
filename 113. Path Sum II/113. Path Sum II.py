# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        answer = []
        def dfs(node,curr_sum,arr):
            if(not node):
                return 

            if curr_sum==targetSum and node.left==None and node.right==None:
                answer.append(arr)

            if node.left:
                dfs(node.left,curr_sum+node.left.val,arr+[node.left.val])

            if node.right:
                dfs(node.right,curr_sum+node.right.val,arr+[node.right.val])
        
        if(root):

            dfs(root,root.val,[root.val])

        return answer
