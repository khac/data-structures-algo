# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/description/


"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        mapGraph = {}
        def dfs(node):
            # print(node.val)
            if node.val in mapGraph:
                return mapGraph[node.val]
            
            mapGraph[node.val] = Node(node.val)
            for neighbour in node.neighbors:
                next_neighbour = dfs(neighbour)
                mapGraph[node.val].neighbors.append(next_neighbour)

            return mapGraph[node.val]

        
        # print(mapGraph)
        return dfs(node)
