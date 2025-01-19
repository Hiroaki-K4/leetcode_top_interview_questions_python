from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for city in range(n):
            if not visited[city]:
                visited[city] = True
                dfs(city)
                provinces += 1

        return provinces


if __name__ == "__main__":
    solution = Solution()
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print("Input: isConnected = {0}".format(isConnected))
    print("Output: {0}".format(solution.findCircleNum(isConnected)))
    print()

    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    print("Input: isConnected = {0}".format(isConnected))
    print("Output: {0}".format(solution.findCircleNum(isConnected)))
