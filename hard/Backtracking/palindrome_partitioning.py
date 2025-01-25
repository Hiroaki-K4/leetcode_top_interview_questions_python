from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])  # Add the current partition to the result
                return

            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)  # Choose the substring
                    backtrack(end, path)  # Explore further
                    path.pop()  # Backtrack

        result = []
        backtrack(0, [])
        return result


if __name__ == "__main__":
    solution = Solution()
    s = "aab"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.partition(s)))
    print()

    s = "a"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.partition(s)))
