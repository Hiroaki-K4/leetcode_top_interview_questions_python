class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort = "".join(sorted(s))
        t_sort = "".join(sorted(t))
        if s_sort == t_sort:
            return True
        return False


if __name__ == "__main__":
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print("Input: s={0}, t={1}".format(s, t))
    print("Output: {0}".format(solution.isAnagram(s, t)))
    print()
    s = "rat"
    t = "car"
    print("Input: s={0}, t={1}".format(s, t))
    print("Output: {0}".format(solution.isAnagram(s, t)))
