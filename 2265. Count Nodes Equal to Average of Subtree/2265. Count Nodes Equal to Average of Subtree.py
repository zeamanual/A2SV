# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.get_count(root)[2]

    def get_count(self,root):

        if(root==None):
            return (0,0,0)
       
        result1 = self.get_count(root.left)
        result2 = self.get_count(root.right)
       
        total_count = result1[0] + result2[0] + 1
        total_sum = result1[1] + result2[1] + root.val
        total_ans = result1[2] + result2[2]

        if( (total_sum // total_count) == root.val ):
            total_ans+=1
        
        return ( total_count,total_sum,total_ans )
