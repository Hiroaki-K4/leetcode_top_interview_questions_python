from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000
        max_profit = 0
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(prices[i] - min_price, max_profit)

        return max_profit


if __name__ == '__main__':
    solution = Solution()
    prices = [7,1,5,3,6,4]
    print("Input: {0}".format(prices))
    print("Output: {0}".format(solution.maxProfit(prices)))
    print()
    prices = [7,6,4,3,1]
    print("Input: {0}".format(prices))
    print("Output: {0}".format(solution.maxProfit(prices)))
