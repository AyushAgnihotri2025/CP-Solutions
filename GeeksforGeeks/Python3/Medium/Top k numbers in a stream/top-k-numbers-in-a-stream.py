#User function Template for python3

class Solution:
    def kTop(self,a, n, k):
        #code here.
        top = [0 for i in range(k + 1)]
        freq = {i:0 for i in range(k + 1)}
        ans=[]
        for m in range(n):
            if a[m] in freq.keys():
                freq[a[m]] += 1
            else:
                freq[a[m]] = 1
            top[k] = a[m]
            i = top.index(a[m])
            i -= 1
            while i >= 0:
                if (freq[top[i]] < freq[top[i + 1]]):
                    t = top[i]
                    top[i] = top[i + 1]
                    top[i + 1] = t
                elif ((freq[top[i]] == freq[top[i + 1]]) and (top[i] > top[i + 1])):
                    t = top[i]
                    top[i] = top[i + 1]
                    top[i + 1] = t
                else:
                    break
                i -= 1
            i = 0
            while i < k and top[i] != 0:
                ans.append(top[i])
                i += 1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.kTop(a,n,k)
    print(*ans)



# } Driver Code Ends