class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        res = "1"
        for i in range(n - 1):
            count = 1
            tmp_res = ""
            for j in range(len(res)):
                if j + 1 < len(res) and res[j] == res[j + 1]:
                    count += 1
                else:
                    tmp_res += str(count) + res[j]
                    count = 1

            res = tmp_res

        return res


if __name__ == "__main__":
    solution = Solution()
    n = 4
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.countAndSay(n)))
    print()

    n = 1
    print("Input: n = {0}".format(n))
    print("Output: {0}".format(solution.countAndSay(n)))
