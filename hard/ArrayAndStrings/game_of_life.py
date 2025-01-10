from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def count_live_neighbors(r, c):
            """Count the number of live neighbors for a given cell."""
            directions = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (board[nr][nc] == 1 or board[nr][nc] == 2)
                ):
                    live_neighbors += 1
            return live_neighbors

        # First pass: Apply rules and mark transitions with temporary states.
        for r in range(rows):
            for c in range(cols):
                live_neighbors = count_live_neighbors(r, c)
                if board[r][c] == 1:  # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2  # Mark as live-to-dead
                elif board[r][c] == 0:  # Dead cell
                    if live_neighbors == 3:
                        board[r][c] = -1  # Mark as dead-to-live

        # Second pass: Finalize states.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0  # Live-to-dead transition
                elif board[r][c] == -1:
                    board[r][c] = 1  # Dead-to-live transition


if __name__ == "__main__":
    solution = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    print("Input: board = {0}".format(board))
    solution.gameOfLife(board)
    print("Output: {0}".format(board))
    print()

    board = [[1, 1], [1, 0]]
    print("Input: board = {0}".format(board))
    solution.gameOfLife(board)
    print("Output: {0}".format(board))
