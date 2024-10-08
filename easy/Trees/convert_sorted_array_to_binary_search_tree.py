# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # Find the middle element
        mid = len(nums) // 2

        # Create the root with the middle element
        root = TreeNode(nums[mid])
        print("root: ", root.val)

        # Recursively build the left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])

        return root
