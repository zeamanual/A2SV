# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if(root1==None and root2==None):
            return True
        elif((root1==None and root2!=None ) or root1!=None and root2==None):
            return False    
        if(root1.val!=root2.val):
            return False
        answer1,answer2 = [],[]

        answer1.append(self.flipEquiv(root1.left,root2.left))
        answer1.append(self.flipEquiv(root1.left,root2.right))

        answer2.append(self.flipEquiv(root1.right,root2.left))
        answer2.append(self.flipEquiv(root1.right,root2.right))

        return all([any(answer1) and any(answer2)])
