from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Add beginWord to the wordList for graph creation
        wordList = set(wordList)
        wordList.add(beginWord)

        # Create a dictionary for intermediate word patterns
        pattern_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                pattern_map[pattern].append(word)

        # BFS initialization
        queue = deque([(beginWord, 1)])  # (current_word, transformation_steps)
        visited = set([beginWord])

        while queue:
            current_word, steps = queue.popleft()

            # Generate all possible intermediate patterns
            for i in range(len(current_word)):
                pattern = current_word[:i] + "*" + current_word[i + 1 :]
                for neighbor in pattern_map[pattern]:
                    if neighbor == endWord:
                        return steps + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))

                # Clear the pattern to prevent redundant checks
                pattern_map[pattern] = []

        return 0


if __name__ == "__main__":
    solution = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(
        "Input: beginWord = {0}, endWord = {1}, wordList = {2}".format(
            beginWord, endWord, wordList
        )
    )
    print("Output: {0}".format(solution.ladderLength(beginWord, endWord, wordList)))
    print()
