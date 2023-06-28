from queue import PriorityQueue
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {i:{} for i in range(n)}
        visited = {i:False for i in range(n)}
        for i in range(len(edges)):
            graph[edges[i][0]][edges[i][1]] = succProb[i]
            graph[edges[i][1]][edges[i][0]] = succProb[i]
        pq = PriorityQueue()
        pq.put((-1, start))
        maxProb = 0
        while not pq.empty():
            weight, node = pq.get()
            if visited[node]: continue
            visited[node] = True
            maxProb = -1 * weight
            if node == end: break
            for child in graph[node]:
                pq.put((weight * graph[node][child], child))
        if node != end:
            return 0
        return maxProb