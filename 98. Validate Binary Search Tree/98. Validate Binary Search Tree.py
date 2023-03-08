# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],min_val = float('-inf'),max_val = float('inf')) -> bool:
        if( root ==None ):
            return True
        elif(root.val >= max_val or root.val <= min_val):
            return False

        left_status = self.isValidBST(root.left,min_val,root.val)
        right_status = self.isValidBST(root.right,root.val,max_val)

        return left_status and right_status
