from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The action nothing can be interpreted at "sell then immediately buy".
        max_profit = 0
        for i in range(len(prices) - 1):
            max_profit += max(prices[i + 1] - prices[i], 0)

        return max_profit


if __name__ == "__main__":
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print("Input: {0}".format(prices))
    print("Output: {0}".format(solution.maxProfit(prices)))
    print()
    prices = [1, 2, 3, 4, 5]
    print("Input: {0}".format(prices))
    print("Output: {0}".format(solution.maxProfit(prices)))
    print()
    prices = [7, 6, 4, 3, 1]
    print("Input: {0}".format(prices))
    print("Output: {0}".format(solution.maxProfit(prices)))
