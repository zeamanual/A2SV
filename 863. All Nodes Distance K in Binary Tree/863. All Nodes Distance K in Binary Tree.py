5# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_dict = {}

        def dfs(node, parent):
            if not node:
                return
            parent_dict[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root,None)

        queue = deque([(target, 0)])
        visited = set()
        res = []

        while queue:
            node, distance = queue.popleft()
            visited.add(node)

            if distance == k:
                res.append(node.val)

            for next_node in (node.left, node.right, parent_dict.get(node)):
                if next_node and next_node not in visited:
                    queue.append((next_node, distance + 1))
                    visited.add(next_node)

        return res
