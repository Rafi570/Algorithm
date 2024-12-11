import heapq
class Solution:
    def dijkstra(self, V, adj, S):
        pq = []
        distTo = [float('inf')] * V
        distTo[S] = 0
        heapq.heappush(pq, (0, S))
        while pq:
            dis, node = heapq.heappop(pq)
            for v, w in adj[node]:
                if dis + w < distTo[v]:
                    distTo[v] = dis + w
                    heapq.heappush(pq, (distTo[v], v))
        return distTo
if __name__ == "__main__":
    V, E, S = 3, 3, 2
    adj = [
        [[1, 1], [2, 6]],
        [[2, 3], [0, 1]],
        [[1, 3], [0, 6]]
    ]
    obj = Solution()
    res = obj.dijkstra(V, adj, S)
    for i in range(V):
        print(res[i], end=" ")
    print()
