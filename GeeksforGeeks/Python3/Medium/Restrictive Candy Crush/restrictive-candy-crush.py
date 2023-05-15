#User function Template for python3

class Solution:
    def Reduced_String(self, k, s):
        # Your code goes here
        # return the reduced string
        if k==1:
            return ""
        stack = []
        n=len(s)
        i=0
        x=0
        while i<n:
            if len(stack)>0 and stack[-1][0]==s[i]:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
                i+=1
            else:
                x=1
                stack.append([s[i],x])
                i+=1
        ans=""
        for i in stack:
            for j in range(i[1]):
                ans+=i[0]
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        k=int(input())
        s=input().strip()
        obj = Solution()
        print(obj.Reduced_String(k,s))

# } Driver Code Ends