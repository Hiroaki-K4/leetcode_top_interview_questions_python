from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, index):
            # Base case: If the entire word is found
            if index == len(word):
                return True

            # Boundary check and character match
            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[0])
                or board[i][j] != word[index]
            ):
                return False

            # Mark the current cell as visited by temporarily modifying the board
            temp = board[i][j]
            board[i][j] = "#"

            # Explore all four possible directions (up, down, left, right)
            found = (
                dfs(i + 1, j, index + 1)
                or dfs(i - 1, j, index + 1)  # Down
                or dfs(i, j + 1, index + 1)  # Up
                or dfs(i, j - 1, index + 1)  # Right
            )  # Left

            # Restore the cell's original value after exploring
            board[i][j] = temp

            return found

        # Traverse every cell in the grid as a potential starting point
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False


if __name__ == "__main__":
    solution = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print("Input: board = {0}, word = {1}".format(board, word))
    print("Output: {0}".format(solution.exist(board, word)))
    print()

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    print("Input: board = {0}, word = {1}".format(board, word))
    print("Output: {0}".format(solution.exist(board, word)))
    print()

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    print("Input: board = {0}, word = {1}".format(board, word))
    print("Output: {0}".format(solution.exist(board, word)))
