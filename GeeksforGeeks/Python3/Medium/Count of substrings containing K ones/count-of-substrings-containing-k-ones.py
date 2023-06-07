#User function Template for python3
class Solution:
    def countOfSubstringWithKOnes(self, S, K):
        # code here
        tot=0
        mp={0:1}
        ans=0
        for i in S:
            if i=="1":
                tot+=1
            # if tot==k:
            #     ans+=1
            if tot-k in mp:
                ans+=mp[tot-k]
            if tot in mp:
                mp[tot]+=1
            else:
                mp[tot]=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        inp = input().strip().split(" ")
        s = inp[0]
        k = int(inp[1])
        ob=Solution()
        print(ob.countOfSubstringWithKOnes(s, k))
# } Driver Code Ends