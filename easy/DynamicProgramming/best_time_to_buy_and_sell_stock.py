from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10 ** 5
        max_profit = 0
        for curr_price in prices:
            min_price = min(curr_price, min_price)
            max_profit = max(curr_price - min_price, max_profit)

        return max_profit


if __name__ == "__main__":
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print("Input: prices = {0}".format(prices))
    print("Output: {0}".format(solution.maxProfit(prices)))
    print()

    prices = [7, 6, 4, 3, 1]
    print("Input: prices = {0}".format(prices))
    print("Output: {0}".format(solution.maxProfit(prices)))
