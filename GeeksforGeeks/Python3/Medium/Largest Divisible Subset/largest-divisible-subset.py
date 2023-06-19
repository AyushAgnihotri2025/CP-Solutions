#User function Template for python3

class Solution:
    def LargestSubset(self, n, arr):
        #Code here
        arr.sort()
        dp=[1]*n
        hash=[0]*n
        lastind=0
        mx=1
        for curr in range(n):
            hash[curr]=curr
            for prev in range(curr):
                if arr[curr]%arr[prev]==0 and dp[curr]<1+dp[prev]:
                    dp[curr]=1+dp[prev]
                    hash[curr]=prev
            if dp[curr]>mx:
                mx=dp[curr]
                lastind=curr
        temp=[]
        temp.append(arr[lastind])
        while hash[lastind]!=lastind:
            lastind=hash[lastind]
            temp.append(arr[lastind])
        return temp


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n=int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.LargestSubset(n,arr)
        isValidSeq, sz = 1, len(res)
        for i in range(sz):
            for j in range(i + 1, sz):
                if (res[i] % res[j] == 0) or (res[j] % res[i] == 0):
                    continue
                else:
                    isValidSeq = 0
                    break
        print(isValidSeq, sz)
# } Driver Code Ends