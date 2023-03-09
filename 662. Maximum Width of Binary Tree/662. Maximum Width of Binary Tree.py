# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        status = defaultdict(list)
        self.solve(root,1,1,status)

        max_width = float('-inf')
        for depth in status.keys():
            max_width = max( max_width, max( status[depth] ) - min( status[depth]) + 1 )

        return max_width

    def solve(self,root,depth,col,status):

        if(root==None):
            return

        status[depth].append(col)
        self.solve(root.left,depth+1,col*2,status)
        self.solve(root.right,depth+1,col*2+1,status)
