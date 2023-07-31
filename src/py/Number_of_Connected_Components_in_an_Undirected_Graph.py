# 323. Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1]*n
    
    def union(self, a, b):
        par_a, par_b = self.find(a), self.find(b)
        if par_a == par_b:
            return False

        self.parent[par_a] = par_b
        self.n -= 1
        return True

    def find(self, a):
        par_a = self.parent[a]
        while par_a != self.parent[par_a]:
            self.parent[par_a] = self.parent[self.parent[par_a]]
            par_a = self.parent[par_a]
        return par_a

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionfind = UnionFind(n)
        for src,dst in edges:
            unionfind.union(src, dst)
        return unionfind.n
