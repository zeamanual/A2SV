# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = [ [] for i in range(2000) ]

        traversed = self.inorder(root)
        max_depth=0
        for node_val,depth in traversed:
            max_depth = max(max_depth,depth)
            ans[depth-1].append(node_val)

        return ans[:max_depth]

    def inorder(self,root,depth=0):

        if(root==None):
            return []

        return self.inorder(root.left,depth+1) + [(root.val,depth+1)] + self.inorder(root.right,depth+1)
