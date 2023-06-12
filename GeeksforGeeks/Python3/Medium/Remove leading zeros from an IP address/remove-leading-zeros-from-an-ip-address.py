#User function Template for python3

class Solution:
    def newIPAdd(self, S):
        # code here
        s=S.split(".")
        ans=""
        for i in s:
            x=i.lstrip("0")
            if x=="":
                x="0"
            ans+=x+"."
        return ans[:len(ans)-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.newIPAdd(s)
        print(ans)
# } Driver Code Ends