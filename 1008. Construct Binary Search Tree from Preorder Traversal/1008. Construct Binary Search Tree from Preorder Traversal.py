# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def build_tree(preorder_traversal):
            if(len(preorder_traversal)==0):
                return None
            root = TreeNode(preorder_traversal[0])

            index=1
            while(index<len(preorder_traversal) and preorder_traversal[index]<preorder_traversal[0]):
                index+=1

            root.left = build_tree(preorder_traversal[1:index])
            root.right = build_tree(preorder_traversal[index:])

            return root

        return build_tree(preorder)
