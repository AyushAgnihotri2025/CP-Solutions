#User function Template for python3

class Solution:
    def search(self, patt, s):
        # code here
        l=[]
        n1=len(s)
        n2=len(patt)
        for i in range(0,n1-n2+1):
            if s[i:i+n2]==patt:
                l.append(i+1)
        return l

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
            print("-1", end = " ")
        else:
            for value in ans:
                print(value,end = ' ')
        print()
# } Driver Code Ends