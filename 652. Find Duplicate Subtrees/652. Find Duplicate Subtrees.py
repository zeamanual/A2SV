# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        def dfs(node):
            if(not node):
                return tuple([None])

            nonlocal visited
            nonlocal answer

            curr = tuple([node.val]) + dfs(node.left) + dfs(node.right)

            visited[(curr)]+=1
            if(curr in visited and visited[curr]==2):
                answer.append(node)
            

            return curr

        visited= defaultdict(int)
        answer = []
        dfs(root)
        return answer
