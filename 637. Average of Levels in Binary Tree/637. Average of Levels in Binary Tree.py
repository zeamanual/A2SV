# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        temp = defaultdict(list)
        que = deque([[root,0]])
        level = 0
        while que:
            curr_node,depth =que.popleft()
            temp[depth].append(curr_node.val)

            if(curr_node.left):
                que.append([curr_node.left,depth+1])

            if(curr_node.right):
                que.append([curr_node.right,depth+1])
            
        index = 0
        ans = []
        while(index in temp):
            ans.append(sum(temp[index])/len(temp[index]))
            index+=1

        return ans
