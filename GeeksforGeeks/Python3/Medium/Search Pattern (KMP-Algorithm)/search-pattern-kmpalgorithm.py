#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        q=[]
        i=0
        while i<=len(txt)-1:
            if pat==txt[i:i+len(pat)]:
                q.append(i+1)
                i+=1
            else:
                i+=1
        if q:
            return q
        return [-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends