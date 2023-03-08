# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        left,right = root.left,root.right

        if(left==None and right==None):
            return True

        elif(left==None or right==None):
            return False
        
        curr_status = left.val == right.val

        new_node1 = TreeNode(0,left.left,right.right)
        new_node2 = TreeNode(0,left.right,right.left)

        return curr_status and self.isSymmetric(new_node1) and self.isSymmetric(new_node2)
