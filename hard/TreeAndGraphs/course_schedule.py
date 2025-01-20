from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list and indegree array
        adj_list = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            indegree[course] += 1

        # Start with all courses with no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited_courses = 0

        while queue:
            current = queue.popleft()
            visited_courses += 1

            for neighbor in adj_list[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If we've visited all courses, it's possible to finish
        return visited_courses == numCourses


if __name__ == "__main__":
    solution = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    print(
        "Input: numCourses = {0}, prerequisites = {1}".format(numCourses, prerequisites)
    )
    print("Output: {0}".format(solution.canFinish(numCourses, prerequisites)))
    print()

    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(
        "Input: numCourses = {0}, prerequisites = {1}".format(numCourses, prerequisites)
    )
    print("Output: {0}".format(solution.canFinish(numCourses, prerequisites)))
