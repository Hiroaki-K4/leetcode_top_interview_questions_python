from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_count = Counter(s1)
        window_count = Counter(s2[:len_s1])

        if s1_count == window_count:
            return True

        for i in range(len_s1, len_s2):
            # Add the new character to the window
            window_count[s2[i]] += 1
            # Remove the old character from the window
            window_count[s2[i - len_s1]] -= 1
            
            # If the count becomes zero, we remove it from the counter
            if window_count[s2[i - len_s1]] == 0:
                del window_count[s2[i - len_s1]]

            # Compare the window with the target frequency
            if s1_count == window_count:
                return True

        return False


if __name__ == '__main__':
    solution = Solution()
    s1 = "ab"
    s2 = "eidbaooo"
    print("Input: s1={0}, s2={1}".format(s1, s2))
    print("Output: {0}".format(solution.checkInclusion(s1, s2)))
    print()
    s1 = "ab"
    s2 = "eidboaoo"
    print("Input: s1={0}, s2={1}".format(s1, s2))
    print("Output: {0}".format(solution.checkInclusion(s1, s2)))
