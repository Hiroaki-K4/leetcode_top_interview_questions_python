from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        tree_deque = deque([root])
        nodes = []
        while tree_deque:
            level_len = len(tree_deque)
            level_nodes = []
            for i in range(level_len):
                current_node = tree_deque.popleft()
                level_nodes.append(current_node.val)
                if current_node.left:
                    tree_deque.append(current_node.left)
                if current_node.right:
                    tree_deque.append(current_node.right)
            nodes.append(level_nodes)

        return nodes
