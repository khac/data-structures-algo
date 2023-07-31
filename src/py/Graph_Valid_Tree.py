# 261. Graph Valid Tree
# https://leetcode.com/problems/graph-valid-tree/

class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1]*n
    
    def union(self, a, b):
        par_a, par_b = self.find(a), self.find(b)
        if par_a == par_b: return False

        self.parent[par_a] = par_b
        return True

    def find(self, a):
        par_a = self.parent[a]
        while par_a != self.parent[par_a]:
            self.parent[par_a] = self.parent[self.parent[par_a]]
            par_a = self.parent[par_a]
        return par_a

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False

        unionFind = UnionFind(n)
        for src,dst in edges:
            if not unionFind.union(src, dst):
                return False
        return True
