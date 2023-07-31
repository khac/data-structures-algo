# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        graph = defaultdict(list)

        for course,prereq in prerequisites:
            indegree[course] += 1
            graph[prereq].append(course)
        
        que = deque()
        coursesTaken = 0
        for i,degree in enumerate(indegree):
            if degree == 0:
                que.append(i)
        
        while que:
            curCourse = que.pop()
            coursesTaken += 1
            for nextCourse in graph[curCourse]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    que.append(nextCourse)

        return coursesTaken == numCourses
