class Solution:
    def firstUniqChar(self, s: str) -> int:
        exist = {}
        first_idx = {}
        for i in range(len(s)):
            if s[i] in exist:
                if s[i] in first_idx:
                    first_idx.pop(s[i])
            else:
                exist[s[i]] = 0
                first_idx[s[i]] = i

        if first_idx == {}:
            return -1

        return next(iter(first_idx.values()))


if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    print("Input: {0}".format(s))
    print("Output: {0}".format(solution.firstUniqChar(s)))
    print()
    s = "loveleetcode"
    print("Input: {0}".format(s))
    print("Output: {0}".format(solution.firstUniqChar(s)))
    print()
    s = "aabb"
    print("Input: {0}".format(s))
    print("Output: {0}".format(solution.firstUniqChar(s)))
