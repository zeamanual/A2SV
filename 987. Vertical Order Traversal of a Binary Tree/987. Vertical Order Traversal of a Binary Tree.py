# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root,matrix,row=0,col=0):
        if(root==None):
            return
        
        matrix[row][col].append(root.val)
        matrix[row][col].sort()
        self.helper(root.left,matrix,row+1,col-1)
        self.helper(root.right,matrix,row+1,col+1)
    def depth(self,root):
        if not root:return 0
        return max(1+self.depth(root.left),1+self.depth(root.right))    


    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic={}
        strech=self.depth(root)
        matrix=[[[] for i in range(2*strech)] for i in range(strech)]
        
        self.helper(root,matrix,0,strech)
        keys=sorted(dic.keys())
        final=[]
        for col in range(len(matrix[0])):
            temp=[]
            for row in range(len(matrix)):
                if matrix[row][col]:
                    temp+=matrix[row][col]
            if temp:
                final.append(temp)
                
        return final
