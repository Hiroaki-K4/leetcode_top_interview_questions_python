from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False

        # Step 1: Determine if first row or first column should be zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                first_row_has_zero = True
                break

        # Step 2: Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 3: Set rows and columns to zero based on the markers
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Step 4: Handle first row and first column separately
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print("Input: matrix = {0}".format(matrix))
    solution.setZeroes(matrix)
    print("Output: {0}".format(matrix))
    print()

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print("Input: matrix = {0}".format(matrix))
    solution.setZeroes(matrix)
    print("Output: {0}".format(matrix))
