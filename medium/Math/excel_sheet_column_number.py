class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0
        for i in range(n - 1, -1, -1):
            count = n - 1 - i
            res += (26 ** count) * (ord(columnTitle[i]) - ord("A") + 1)
        return res


if __name__ == "__main__":
    solution = Solution()
    columnTitle = "A"
    print("Input: columnTitle = {0}".format(columnTitle))
    print("Output: {0}".format(solution.titleToNumber(columnTitle)))
    print()

    columnTitle = "AB"
    print("Input: columnTitle = {0}".format(columnTitle))
    print("Output: {0}".format(solution.titleToNumber(columnTitle)))
    print()

    columnTitle = "ZY"
    print("Input: columnTitle = {0}".format(columnTitle))
    print("Output: {0}".format(solution.titleToNumber(columnTitle)))
