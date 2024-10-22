# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = deque()

            for _ in range(level_size):
                node = queue.popleft()
                # Add node's value in the appropriate order
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)

                # Add child nodes for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the current level to the result
            result.append(list(current_level))
            # Toggle the traversal direction
            left_to_right = not left_to_right

        return result
