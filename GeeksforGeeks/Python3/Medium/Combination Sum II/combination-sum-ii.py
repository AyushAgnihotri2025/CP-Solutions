#User function Template for python3

class Solution:
    def combinationSum2(self, candidates, target):
        # Code here
        def helper(t,curr,ind):
            if(t==0):
                ans.append(curr.copy())
                return
            for i in range(ind,len(candidates)):
                if(i>ind and candidates[i]==candidates[i-1]):
                    continue
                if(candidates[i]>t):
                    break
                curr.append(candidates[i])
                helper(t-candidates[i],curr,i+1)
                curr.pop()
     
        candidates.sort()
        ans,curr=[],[]
        helper(target,curr,0)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, target = list(map(int, input().split()))
        candidates = list(map(int, input().split()))
        ob = Solution()
        res = ob.combinationSum2(candidates, target)
        res.sort()
        print('[ ', end = '')
        for subset in res:
            print('[ ', end = '')
            for val in subset:
                print(val, end = ' ')
            print(']', end = '')
        print(' ]')
# } Driver Code Ends