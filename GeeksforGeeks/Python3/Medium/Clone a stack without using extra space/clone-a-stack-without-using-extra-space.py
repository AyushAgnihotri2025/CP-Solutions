#User function Template for python3

class Solution:
    def clonestack(self, st, cloned):
        # code here
        n = len(st)
        m = n-1
        for i in range(n-1):
            temp = st.pop()
            for j in range(m):
                cloned.append(st.pop())
            st.append(temp)
            for j in range(m):
                st.append(cloned.pop())
            m-=1
        while (st):
            cloned.append(st.pop())

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import deque

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        st=deque()
        copy=[]
        
        for i in range(N):
            st.append(arr[i])
            copy.append(arr[i])
        
        copy = copy[::-1]
            
        cloned=deque()
        
        ob = Solution()
        
        ob.clonestack(st,cloned)
        
        check=[]
        
        while len(cloned):
            check.append(cloned.pop())
        
        flag = 0
        
        if copy != check:
            flag = 1
        
        print(1-flag)
# } Driver Code Ends