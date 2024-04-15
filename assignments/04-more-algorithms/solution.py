from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}

        for prereq in prerequisites:
            adj_list[prereq[0]].append(prereq[1])

        visited = set()
        path = list()

        def dfs(course: int) -> bool:
            if course in visited:
                return False
            if course in path:
                return True
            if adj_list[course] == []:
                path.append(course)
                return True
            visited.add(course)
            for adj in adj_list[course]:
                if not dfs(adj):
                    return False
            path.append(course)
            adj_list[course] == []
            visited.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return path
