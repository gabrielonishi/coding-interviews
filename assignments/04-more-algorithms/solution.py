'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid 
answers, return any of them. If it is impossible to finish all courses, return an empty array. 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished 
course 0. So the correct course order is [0,1].

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished 
both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one 
correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

Example 4:
Input: numCourses = 4, prerequisites = [[0, 3], [0, 1], [3, 2], [1, 2]]

prereqs = {
    0 : {3, 1}
    1 : {2}
    2 : {}
    3 : {2}
}

[2]
'''
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        order_of_courses = list()

        prereq_dict = {i: set() for i in range(numCourses)}

        for prereq in prerequisites:
            prereq_dict[prereq[1]].add(prereq[0])

        for i in range(numCourses):
            if len(prereq_dict[i]) == 0:
                order_of_courses.append(prereq)
                break

        if len(order_of_courses) == 0:
            return []

        counter = 1
