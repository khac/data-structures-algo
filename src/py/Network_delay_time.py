# Network delay time
# Dijkstra's Algorithm
# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        min_dist = [inf]*n
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append([w,v])
        min_heap = [[0,k]]
        visited = 0
        while min_heap:
            w,v = heappop(min_heap)
            if min_dist[v-1] <= w: continue
            min_dist[v-1] = min(w, min_dist[v-1])
            if visited == n: break
            for next_w, next_v in graph[v]:
                heappush(min_heap, [next_w+min_dist[v-1], next_v])
        # print(min_dist)
        return max(min_dist) if max(min_dist) != inf else -1
