# 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        """
            [[0,0],[2,2],[3,10],[5,2],[7,0]]

            [[13, [3,10]], [7, [5,2]], [7, [7,0]]] set([0])
            [[13, [3,10]], [7, [5,2]], [7, [7,0]], [9, [3,10]], [7, [7,0]]] set([0,1]) 
            [[13, [3,10]], [9, [3,10]], [7, [7,0]], [10, [3,10]], [14, [7,0]]] set([0,1,3]) 
            [[13, [3,10]], [9, [3,10]], [7, [7,0]], [10, [3,10]], [14, [7,0]]] set([0,1,3,5])
            [[13, [3,10]], [10, [3,10]], [14, [7,0]]] set([0,1,3,5,2])
        """

        visited, total_cost,n = set(), 0, len(points)
        min_heap = [[0,0]]

        def cost(i,j):
            return abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])

        while len(visited) != n:
            cur_cost, index = heappop(min_heap)
            if index in visited:
                continue
            visited.add(index)
            total_cost += cur_cost
            if len(visited) == n: break
            for next_node in range(n):
                if next_node not in visited:
                    heappush(min_heap, [cost(index, next_node), next_node])

        return total_cost

