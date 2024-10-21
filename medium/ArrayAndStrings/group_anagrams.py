from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for target_str in strs:
            # Sort string
            str_list = []
            for s in target_str:
                str_list.append(s)
            str_list.sort()

            # Detect anagrams
            ana = ""
            for s in str_list:
                ana += s
            if ana in anagrams:
                anagrams[ana].append(target_str)
            else:
                anagrams[ana] = [target_str]

        ans_list = []
        for key, value in anagrams.items():
            ans_list.append(value)

        return ans_list


if __name__ == "__main__":
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Input: strs = {0}".format(strs))
    print("Output: {0}".format(solution.groupAnagrams(strs)))
    print()

    strs = [""]
    print("Input: strs = {0}".format(strs))
    print("Output: {0}".format(solution.groupAnagrams(strs)))
    print()

    strs = ["a"]
    print("Input: strs = {0}".format(strs))
    print("Output: {0}".format(solution.groupAnagrams(strs)))
