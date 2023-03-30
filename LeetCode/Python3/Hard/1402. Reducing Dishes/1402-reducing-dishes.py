class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # Sort satisfaction levels in ascending order
        satisfaction.sort()
        n = len(satisfaction)
        # Initialize memoization table with default value of negative infinity
        mem = [[-float('inf')] * (n + 1) for _ in range(n)]
        
        def dp(start, num):
            # Base case: if we have considered all dishes, return 0
            if start >= n:
                return 0
            # If the result for this subproblem has not been computed yet, compute it
            if mem[start][num] == -float('inf'):
                # Two choices: prepare the current dish or discard it
                mem[start][num] = max(
                    # Prepare the current dish and recursively compute the maximum satisfaction for the remaining dishes
                    satisfaction[start] * num + dp(start + 1, num + 1),
                    # Discard the current dish and recursively compute the maximum satisfaction for the remaining dishes
                    dp(start + 1, num)
                )
            # Return the result for this subproblem
            return mem[start][num]
        
        # Start the dynamic programming algorithm with the first dish and one dish prepared so far
        return dp(0, 1)