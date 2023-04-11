# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.answer_list = []
        self.traverse(root,[])
        
        path_sum = 0
        for path in self.answer_list:
            path = ''.join(list(map(str,path)))
            path_sum += int(path)
        
        return path_sum
    
    def traverse(self,root,curr_path):
        if(root==None):
            return
        elif(root.left == None and root.right == None):
            self.answer_list.append(curr_path.copy()+[root.val])
            return 

        curr_path.append(root.val)

        self.traverse(root.left,curr_path)
        self.traverse(root.right,curr_path)

        curr_path.pop()
