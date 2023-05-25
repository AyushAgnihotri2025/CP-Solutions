from collections import deque
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if n >= k + maxPts:
            return 1        
        prob = 1.0
        summ = float(n - k + 1)
        q = deque([1] * (n - k + 1))
        for i in reversed(range(k)): 
            prob = summ / maxPts
            q.append(prob)
            summ += prob
            if len(q) > maxPts:
                summ -= q.popleft()
        return prob