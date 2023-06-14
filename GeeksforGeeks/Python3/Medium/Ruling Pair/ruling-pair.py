#User function Template for python3

#Back-end complete function Template for Python 3


class Solution:
    def RulingPair(self, arr, n): 
    	# Your code goes here
        def su(n):
           r = 0
           while n:
               r, n = r + n % 10, n // 10
           return r

        m = -1
        h = {}
        for a in arr:
            t = a 
            s = su(a)
            if s in h:
                m = max(m, a + h[s])
                if t > h[s]:
                    h[s] = t
            else:
                h[s] = a
        return m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        obj = Solution();
        print(obj.RulingPair(arr,n))



# } Driver Code Ends