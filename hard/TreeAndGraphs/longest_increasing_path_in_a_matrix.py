from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:  # Edge case: empty matrix
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]  # Memoization table

        def dfs(x, y):  # Recursive DFS function
            if dp[x][y] != -1:  # Already computed
                return dp[x][y]

            max_length = 1  # At least the cell itself
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

            for dx, dy in directions:  # Explore neighbors
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    max_length = max(max_length, 1 + dfs(nx, ny))

            dp[x][y] = max_length  # Store result
            return dp[x][y]

        max_path = 0
        for i in range(m):  # Try all cells
            for j in range(n):
                max_path = max(max_path, dfs(i, j))

        return max_path


if __name__ == "__main__":
    solution = Solution()
    matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    print("Input: matrix = {0}".format(matrix))
    print("Output: {0}".format(solution.longestIncreasingPath(matrix)))
    print()

    matrix = [[1]]
    print("Input: matrix = {0}".format(matrix))
    print("Output: {0}".format(solution.longestIncreasingPath(matrix)))
