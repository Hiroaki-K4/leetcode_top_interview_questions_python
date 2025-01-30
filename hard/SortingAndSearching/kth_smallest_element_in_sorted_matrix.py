from typing import List


class Solution:
    def count_less_equal(self, matrix, mid, n):
        count = 0
        row, col = n - 1, 0  # Start from bottom-left
        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1  # All elements above this are also ≤ mid
                col += 1
            else:
                row -= 1
        return count

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n - 1][n - 1]

        while low < high:
            mid = (low + high) // 2
            if self.count_less_equal(matrix, mid, n) < k:
                low = mid + 1
            else:
                high = mid

        return low


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print("Input: matrix = {0}, k = {1}".format(matrix, k))
    print("Output: {0}".format(solution.kthSmallest(matrix, k)))
    print()

    matrix = [[-5]]
    k = 1
    print("Input: matrix = {0}, k = {1}".format(matrix, k))
    print("Output: {0}".format(solution.kthSmallest(matrix, k)))
