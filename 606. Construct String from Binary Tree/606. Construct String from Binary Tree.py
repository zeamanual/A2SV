# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.traverse(root)

    def traverse(self,root):

        if(root == None):
            return ''
        
        if(root.left == None and root.right == None):
            return f"{root.val}"
        elif(root.right == None):
            return f"{root.val}({self.traverse(root.left)})" 

        return f"{root.val}({self.traverse(root.left)})({self.traverse(root.right)})" 
