# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        curr_sum = None
        left_nodes = [None, None]
        right_nodes = [None, None]
        
        if(root1):
            curr_sum=root1.val
            left_nodes[0]=root1.left
            right_nodes[0] = root1.right

        if(root2):
            curr_sum = curr_sum + root2.val if curr_sum!=None else root2.val
            left_nodes[1]=root2.left
            right_nodes[1] =root2.right

        if(curr_sum==None):
            return None

        root = TreeNode(curr_sum)
        root.left = self.mergeTrees(left_nodes[0],left_nodes[1])
        root.right = self.mergeTrees(right_nodes[0],right_nodes[1])

        return root
