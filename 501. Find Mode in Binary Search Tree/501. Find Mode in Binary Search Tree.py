# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
       
        dic = {}
        self.inorder(root,dic)
        highest_freq = max(dic.values())
        answer = filter( lambda key: dic[key] == highest_freq, dic.keys() )

        return answer
    
    def inorder(self,root,dic):
        if(root==None):
            return 
        dic[root.val]=dic.get(root.val,0) + 1
        self.inorder(root.left,dic)
        self.inorder(root.right,dic)
