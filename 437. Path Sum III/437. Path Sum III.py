# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.prefix_sum = defaultdict(int)
        self.prefix_sum[0]=1
        self.get_count(root,0,targetSum)
        return self.count


    def get_count(self,root,curr_sum,target_sum):

        if(root==None):
            return
            
        curr_sum+=root.val
        if(curr_sum-target_sum in self.prefix_sum):
            self.count += self.prefix_sum[curr_sum-target_sum]
        
        self.prefix_sum[curr_sum]+=1

        left_count = self.get_count(root.left,curr_sum,target_sum)
        right_count = self.get_count(root.right,curr_sum,target_sum)

        self.prefix_sum[curr_sum]-=1

        return 
