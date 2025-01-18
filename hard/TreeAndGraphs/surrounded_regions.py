from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        # Helper function for DFS
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "T"  # Mark as temporary safe
            # Explore neighbors
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # Step 1: Mark all boundary-connected 'O's as safe
        for r in range(rows):
            for c in (0, cols - 1):  # First and last column
                if board[r][c] == "O":
                    dfs(r, c)
        for c in range(cols):
            for r in (0, rows - 1):  # First and last row
                if board[r][c] == "O":
                    dfs(r, c)

        # Step 2: Replace all 'O' with 'X', and 'T' back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


if __name__ == "__main__":
    solution = Solution()
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    print("Input: board = {0}".format(board))
    solution.solve(board)
    print("Output: {0}".format(board))
    print()

    board = [["X"]]
    print("Input: board = {0}".format(board))
    solution.solve(board)
    print("Output: {0}".format(board))
