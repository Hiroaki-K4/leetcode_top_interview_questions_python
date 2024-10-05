# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_symmetric_tree(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if (root1 is None and not root2 is None) or (
            not root1 is None and root2 is None
        ):
            return False

        if root1.val == root2.val:
            return self.check_symmetric_tree(
                root1.left, root2.right
            ) and self.check_symmetric_tree(root1.right, root2.left)
        return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check_symmetric_tree(root.left, root.right)
