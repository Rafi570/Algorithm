def dijkstra(V, adj, S):
    st = set()
    dist = [float('inf')] * V
    dist[S] = 0
    st.add((0, S))

    while st:
        dis, node = min(st)
        st.remove((dis, node))

        for adjNode, edgeWeight in adj[node]:
            if dis + edgeWeight < dist[adjNode]:
                if dist[adjNode] != float('inf'):
                    st.discard((dist[adjNode], adjNode))

                
                dist[adjNode] = dis + edgeWeight
                st.add((dist[adjNode], adjNode))

    return dist

if __name__ == "__main__":
    V, E, S = 3, 3, 2

    adj = [[] for _ in range(V)]
    adj[0].append((1, 1))
    adj[0].append((2, 6))
    adj[1].append((2, 3))
    adj[1].append((0, 1))
    adj[2].append((1, 3))
    adj[2].append((0, 6))

    result = dijkstra(V, adj, S)
    print(" ".join(map(str, result)))
