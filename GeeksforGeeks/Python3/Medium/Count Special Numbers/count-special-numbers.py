#User function Template for python3

class Solution:
    def countSpecialNumbers(self, N, arr):
        # Code here
        m = max(arr)
        res = [0]*(m+1)
        for a in arr:
            if res[a] <= 1:
                for b in range(a, m+1, a):
                    res[b] += 1
        return sum(res[a] > 1 for a in arr)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N=int(input())
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.countSpecialNumbers(N, arr))
        
        T -= 1
# } Driver Code Ends