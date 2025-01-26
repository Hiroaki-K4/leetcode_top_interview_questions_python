from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(row, col, node, path):
            # Out of bounds, already visited, or no path in Trie
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or visited[row][col]
                or board[row][col] not in node.children
            ):
                return

            char = board[row][col]
            visited[row][col] = True
            node = node.children[char]
            path += char

            # If it is a word, add it to the result
            if node.is_word:
                result.add(path)

            # Explore all 4 directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(row + dr, col + dc, node, path)

            # Backtrack
            visited[row][col] = False

        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root, "")

        return list(result)


if __name__ == "__main__":
    solution = Solution()
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"],
    ]
    words = ["oath", "pea", "eat", "rain"]
    print("Input: board = {0}, words = {1}".format(board, words))
    print("Output: {0}".format(solution.findWords(board, words)))
    print()

    board = [["a", "b"], ["c", "d"]]
    words = ["abcb"]
    print("Input: board = {0}, words = {1}".format(board, words))
    print("Output: {0}".format(solution.findWords(board, words)))
