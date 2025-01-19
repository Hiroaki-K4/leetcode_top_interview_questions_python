# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")  # Global variable to track the maximum path sum

        def dfs(node):
            if not node:
                return 0

            # Recursively find the maximum path sum of left and right subtrees
            left_max = max(dfs(node.left), 0)  # Ignore negative paths
            right_max = max(dfs(node.right), 0)

            # Compute the maximum path sum with a split at the current node
            current_sum = node.val + left_max + right_max

            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_sum)

            # Return the maximum path sum without a split, to be used by the parent
            return node.val + max(left_max, right_max)

        dfs(root)
        return self.max_sum
