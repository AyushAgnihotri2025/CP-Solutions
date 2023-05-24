class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        sol = [0] * (n+1)
        sol[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                sol[i] += sol[j] * sol[i-j-1]
        return sol[n]