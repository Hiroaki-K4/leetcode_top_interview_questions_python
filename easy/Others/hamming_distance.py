class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        while xor:
            count += xor & 1
            xor >>= 1

        return count


if __name__ == "__main__":
    solution = Solution()
    x = 1
    y = 4
    print("Input: x = {0}, y = {1}".format(x, y))
    print("Output: {0}".format(solution.hammingDistance(x, y)))
    print()

    x = 3
    y = 1
    print("Input: x = {0}, y = {1}".format(x, y))
    print("Output: {0}".format(solution.hammingDistance(x, y)))
