# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper(node):
            if not node:
                return ["#"]
            return [str(node.val)] + helper(node.left) + helper(node.right)

        return ",".join(helper(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper(values):
            if not values:
                return None
            val = values.pop(0)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = helper(values)
            node.right = helper(values)
            return node

        values = data.split(",")
        return helper(values)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    serialized = codec.serialize(root)
    print("Serialized Tree:", serialized)  # Output: "1,2,#,#,3,4,#,#,5,#,#"

    deserialized = codec.deserialize(serialized)

    # Verify by serializing again
    print(
        "Serialized Again:", codec.serialize(deserialized)
    )  # Should match the original serialized string
