# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        answer = None
        def helper(node):
            nonlocal answer
            if(not node):
                return []

            res = []
            if(node == p or node == q):
                res.append(node)

            res+=helper(node.left)
            res+=helper(node.right)

            if(not answer and len(res)==2):
                answer=node

            return res

        helper(root)
        return answer
