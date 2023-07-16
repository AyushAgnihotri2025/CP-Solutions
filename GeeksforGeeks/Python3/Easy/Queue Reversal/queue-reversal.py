#User function Template for python3

class Solution:
    #Function to reverse the queue.
    def rev(self, q):
        #add code here
        st=[]
        while (not q.empty()):
            frnt=q.get()
            st.append(frnt)
        while len(st)!=0:
            top=st.pop()
            q.put(top)
        return q

#{ 
 # Driver Code Starts

#Initial Template for Python 3

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n)
        for j in a:
            q.put(j)
            
        ob = Solution()
        q=ob.rev(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()
# } Driver Code Ends