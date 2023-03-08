# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        answer = [[] for i in range(100)]
        max_depth = self.traversal(root,0,answer)

        return answer[:max_depth]

    
    def traversal(self,root,depth=0,answer=[]):

        if(root==None):
            return 0
        answer[depth]=root.val
        left_depth =  self.traversal(root.left,depth+1,answer)
        right_depth = self.traversal(root.right,depth+1,answer)

        return max(1+left_depth,1+right_depth)
