from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize the dp array
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins to make amount 0

        # Build up the dp array
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still amount + 1, it's not possible to make that amount
        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == "__main__":
    solution = Solution()
    coins = [1, 2, 5]
    amount = 11
    print("Input: coins = {0}, amount = {1}".format(coins, amount))
    print("Output: {0}".format(solution.coinChange(coins, amount)))
    print()

    coins = [2]
    amount = 3
    print("Input: coins = {0}, amount = {1}".format(coins, amount))
    print("Output: {0}".format(solution.coinChange(coins, amount)))
    print()

    coins = [1]
    amount = 0
    print("Input: coins = {0}, amount = {1}".format(coins, amount))
    print("Output: {0}".format(solution.coinChange(coins, amount)))
