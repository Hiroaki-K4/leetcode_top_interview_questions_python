# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(
        self,
        root: Optional[TreeNode],
        smaller_than=float("inf"),
        larger_than=float("-inf"),
    ) -> bool:
        if root is None:
            return True
        if root.val <= larger_than or root.val >= smaller_than:
            return False
        return self.isValidBST(root.left, root.val, larger_than) and self.isValidBST(
            root.right, smaller_than, root.val
        )
