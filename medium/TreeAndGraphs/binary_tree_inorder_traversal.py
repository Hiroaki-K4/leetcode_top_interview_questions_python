# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if node is None:
                return
            # Visit left subtree
            inorder(node.left)
            # Visit current node
            result.append(node.val)
            # Visit right subtree
            inorder(node.right)

        inorder(root)
        return result
