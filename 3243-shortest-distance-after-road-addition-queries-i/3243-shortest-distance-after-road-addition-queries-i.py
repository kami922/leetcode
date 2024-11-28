class Solution:
    def __init__(self):
        self.graph = []

    def bfs(self, n: int) -> int:
        q = deque([0])
        dist = [float('inf')] * n
        dist[0] = 0
        visited = set([0])

        while q:
            node = q.popleft()
            if node == n - 1:
                return dist[node]
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dist[neighbor] = dist[node] + 1
                    q.append(neighbor)
                    visited.add(neighbor)
        return -1

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        self.graph = [[] for _ in range(n)]
        for i in range(n - 1):
            self.graph[i].append(i + 1)
        res = []
        for query in queries:
            self.graph[query[0]].append(query[1])
            res.append(self.bfs(n))
        return res