from collections import deque
from typing import List


class Solution:
    def is_valid(self, s):
        count = 0
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            if count < 0:
                return False
        return count == 0

    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]

        # BFS setup
        queue = deque([s])
        visited = set([s])
        result = []
        found = False

        while queue:
            current = queue.popleft()

            if self.is_valid(current):
                result.append(current)
                found = True

            if found:
                continue

            # Generate all possible states
            for i in range(len(current)):
                # Skip letters
                if current[i] not in "()":
                    continue
                # Remove the current parenthesis
                next_state = current[:i] + current[i + 1 :]
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append(next_state)

        return result


if __name__ == "__main__":
    solution = Solution()
    s = "()())()"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.removeInvalidParentheses(s)))
    print()

    s = "(a)())()"
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.removeInvalidParentheses(s)))
    print()

    s = ")("
    print("Input: s = {0}".format(s))
    print("Output: {0}".format(solution.removeInvalidParentheses(s)))
