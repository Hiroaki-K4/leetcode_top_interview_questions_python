from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check column
        for row in range(9):
            store_dict = {}
            for i in range(1, 10):
                store_dict[str(i)] = 0
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if store_dict[num] >= 1:
                    return False
                else:
                    store_dict[num] += 1

        # Check row
        for col in range(9):
            store_dict = {}
            for i in range(1, 10):
                store_dict[str(i)] = 0
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if store_dict[num] >= 1:
                    return False
                else:
                    store_dict[num] += 1

        # Check 3*3 sub-boxes
        for row_start in range(0, 7, 3):
            for col_start in range(0, 7, 3):
                store_dict = {}
                for i in range(1, 10):
                    store_dict[str(i)] = 0
                for row in range(row_start, row_start + 3):
                    for col in range(col_start, col_start + 3):
                        num = board[row][col]
                        if num == ".":
                            continue
                        if store_dict[num] >= 1:
                            return False
                        else:
                            store_dict[num] += 1

        return True


if __name__ == "__main__":
    solution = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print("Input: board={0}".format(board))
    print("Output: {0}".format(solution.isValidSudoku(board)))
    print()
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print("Input: board={0}".format(board))
    print("Output: {0}".format(solution.isValidSudoku(board)))
