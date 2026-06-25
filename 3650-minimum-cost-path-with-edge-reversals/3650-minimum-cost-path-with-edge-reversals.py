import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list:
        # - original edges u->v cost w
        # - reversed-use edges u->v cost 2w (where original was v->u cost w)
        graph = [[] for _ in range(n)]
        
        for u, v, w in edges:
            graph[u].append((v, w))       # normal forward edge
            graph[v].append((u, 2 * w))   # switch-reversal: from v, can "reverse" this edge to go to u... 
        
        # dist array
        dist = [float('inf')] * n
        dist[0] = 0
        pq = [(0, 0)]  # (cost, node)
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            if u == n - 1:
                return d
            for v, w in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))
        
        return dist[n - 1] if dist[n - 1] != float('inf') else -1