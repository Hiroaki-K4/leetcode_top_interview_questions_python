from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        # Generate each row of the Pascal's triangle
        for i in range(numRows):
            # Start each row with 1
            row = [1] * (i + 1)

            # Each element (except the first and last) is the sum of the two numbers above it
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle


if __name__ == "__main__":
    solution = Solution()
    numRows = 5
    print("Input: numRows = {0}".format(numRows))
    print("Output: {0}".format(solution.generate(numRows)))
    print()

    solution = Solution()
    numRows = 1
    print("Input: numRows = {0}".format(numRows))
    print("Output: {0}".format(solution.generate(numRows)))
