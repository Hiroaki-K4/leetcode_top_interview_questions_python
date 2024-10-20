class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        curr_idx = 0
        while curr_idx < len(s):
            roman = s[curr_idx]
            if roman == "I":
                if curr_idx + 1 < len(s) and s[curr_idx + 1] == "V":
                    count += 4
                    curr_idx += 2
                elif curr_idx + 1 < len(s) and s[curr_idx + 1] == "X":
                    count += 9
                    curr_idx += 2
                else:
                    count += 1
                    curr_idx += 1
            elif roman == "V":
                count += 5
                curr_idx += 1
            elif roman == "X":
                if curr_idx + 1 < len(s) and s[curr_idx + 1] == "L":
                    count += 40
                    curr_idx += 2
                elif curr_idx + 1 < len(s) and s[curr_idx + 1] == "C":
                    count += 90
                    curr_idx += 2
                else:
                    count += 10
                    curr_idx += 1
            elif roman == "L":
                count += 50
                curr_idx += 1
            elif roman == "C":
                if curr_idx + 1 < len(s) and s[curr_idx + 1] == "D":
                    count += 400
                    curr_idx += 2
                elif curr_idx + 1 < len(s) and s[curr_idx + 1] == "M":
                    count += 900
                    curr_idx += 2
                else:
                    count += 100
                    curr_idx += 1
            elif roman == "D":
                count += 500
                curr_idx += 1
            elif roman == "M":
                count += 1000
                curr_idx += 1

        return count


if __name__ == "__main__":
    solution = Solution()
    s = "III"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.romanToInt(s)))
    print()

    s = "LVIII"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.romanToInt(s)))
    print()

    s = "MCMXCIV"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.romanToInt(s)))
