#User function Template for python3

class Solution:
    def combinationSum(self, K, target):
        # Code here
        def backtrack(remaining, k, path, start):
            if remaining == 0 and k == 0:
                combinations.append(path[:])
                return
            if remaining < 0 or k == 0:
                return
            for i in range(start, 10):
                path.append(i)
                backtrack(remaining - i, k - 1, path, i + 1)
                path.pop()
        combinations = []
        backtrack(target, K, [], 1)
        return combinations

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        K, N = list(map(int, input().split()))
        ob = Solution()
        ans = ob.combinationSum(K, N)
        for combination in ans:
            for val in combination:
                print(val, end = ' ')
            print()
# } Driver Code Ends