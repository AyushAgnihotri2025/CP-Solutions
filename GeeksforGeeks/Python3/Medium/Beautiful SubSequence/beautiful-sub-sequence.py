#User function Template for python3

class Solution:
    def longest_Subsequence (self,arr, n) : 
        #Complete the function
        arr.sort()
        mp = {}
        result = {}
        soln = 0
        for i in range(n):
            if arr[i] in mp:
                mp[arr[i]] += 1
            else:
                mp[arr[i]] = 1
        
        for i in range(n-1, -1, -1):
            count = 0
            for j in range(2*arr[i], arr[n-1]+1, arr[i]):
                if j in mp:
                    count = max(count, result[j])
            result[arr[i]] = mp[arr[i]] + count
            soln = max(soln, result[arr[i]])

        if soln <= 1:
            return -1
        return soln

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.longest_Subsequence(arr, n))




# } Driver Code Ends