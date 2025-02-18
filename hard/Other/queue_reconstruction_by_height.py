from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort by height in descending order, and by k in ascending order for same height
        people.sort(key=lambda x: (-x[0], x[1]))

        # Step 2: Insert into queue based on k value
        queue = []
        for person in people:
            queue.insert(person[1], person)  # Insert at index k
        return queue


if __name__ == "__main__":
    solution = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print("Input: people = {0}".format(people))
    print("Output: {0}".format(solution.reconstructQueue(people)))
    print()

    people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    print("Input: people = {0}".format(people))
    print("Output: {0}".format(solution.reconstructQueue(people)))
