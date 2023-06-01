# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @lru_cache(None)
        def get_max(node):
            if(not node):
                return 0

            # stealing current home
            sum1 = node.val

            if(node.right):
                sum1 +=get_max(node.right.right)
                sum1 += get_max(node.right.left)

            if(node.left):
                sum1 += get_max(node.left.left)
                sum1 += get_max(node.left.right)

            # skipping the current home
            sum2 = 0
            sum2+=get_max(node.left)
            sum2+=get_max(node.right)

            return max(sum1,sum2)

        return get_max(root)
