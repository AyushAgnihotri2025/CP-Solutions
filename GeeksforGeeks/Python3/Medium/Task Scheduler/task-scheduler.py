#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def leastInterval(self, N, K, tasks):
        # Code here
        cnt = [0]*26
        for c in tasks:
            cnt[ord(c)-ord('A')] += 1
        cnt.sort(reverse=True)
        m = cnt[0]-1
        slots = m*K
        for i in range(1, 26):
            slots -= min(m, cnt[i])
        slots = max(0, slots)
        return len(tasks)+slots

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, K = list(map(int, input().split()))
        tasks = input().split()
        ob = Solution()
        res = ob.leastInterval(N, K, tasks)
        print(res)
# } Driver Code Ends