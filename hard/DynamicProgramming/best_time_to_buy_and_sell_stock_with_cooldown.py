from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        hold, sold, cooldown = -prices[0], 0, 0

        for i in range(1, n):
            new_hold = max(hold, cooldown - prices[i])
            new_sold = hold + prices[i]
            new_cooldown = max(cooldown, sold)

            hold, sold, cooldown = new_hold, new_sold, new_cooldown

        return max(sold, cooldown)


if __name__ == "__main__":
    solution = Solution()
    prices = [1, 2, 3, 0, 2]
    print("Input: prices = {0}".format(prices))
    print("Output: {0}".format(solution.maxProfit(prices)))
    print()

    prices = [1]
    print("Input: prices = {0}".format(prices))
    print("Output: {0}".format(solution.maxProfit(prices)))
