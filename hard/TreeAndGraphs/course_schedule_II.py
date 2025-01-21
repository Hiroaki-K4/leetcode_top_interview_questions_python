from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create adjacency list and in-degree array
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        # Step 2: Initialize the queue with courses having in-degree 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        course_order = []

        # Step 3: Process courses
        while queue:
            course = queue.popleft()
            course_order.append(course)

            # Reduce in-degree for neighbors
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses are processed
        if len(course_order) == numCourses:
            return course_order
        else:
            return []


if __name__ == "__main__":
    solution = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    print(
        "Input: numCourses = {0}, prerequisites = {1}".format(numCourses, prerequisites)
    )
    print("Output: {0}".format(solution.canFinish(numCourses, prerequisites)))
    print()

    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(
        "Input: numCourses = {0}, prerequisites = {1}".format(numCourses, prerequisites)
    )
    print("Output: {0}".format(solution.canFinish(numCourses, prerequisites)))
    print()

    numCourses = 1
    prerequisites = []
    print(
        "Input: numCourses = {0}, prerequisites = {1}".format(numCourses, prerequisites)
    )
    print("Output: {0}".format(solution.canFinish(numCourses, prerequisites)))
