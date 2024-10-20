class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False

        return sum(is_prime)


if __name__ == "__main__":
    solution = Solution()
    n = 10
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.countPrimes(n)))
    print()

    n = 0
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.countPrimes(n)))
    print()

    n = 1
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.countPrimes(n)))
