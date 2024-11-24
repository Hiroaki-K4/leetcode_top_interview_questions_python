class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Digit-to-letters mapping
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        # Backtracking function
        def backtrack(index: int, current_combination: str):
            # If the combination is complete, add it to the result
            if index == len(digits):
                result.append(current_combination)
                return

            # Get the letters corresponding to the current digit
            letters = phone_map[digits[index]]

            # Explore all possible letters for the current digit
            for letter in letters:
                backtrack(index + 1, current_combination + letter)

        # Start backtracking from the first digit
        backtrack(0, "")
        return result
