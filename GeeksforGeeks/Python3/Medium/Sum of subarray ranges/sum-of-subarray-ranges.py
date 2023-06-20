#User function Template for python3

class Solution:
    def subarrayRanges(self, N, arr):
        # Code here
        prev=[-1]*N
        res=[0]*N
        st=[]
        for i in range(N):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if st:
                prev[i]=st[-1]
            st.append(i)
        for i in range(N):
            index=(res[prev[i]] or 0)
            res[i]=index+(i-prev[i])*arr[i]
        mins=sum(res)
        prev=[-1]*N
        res=[0]*N
        st=[]
        for i in range(N):
            while st and arr[st[-1]]<arr[i]:
                st.pop()
            if st:
                prev[i]=st[-1]
            st.append(i)
        for i in range(N):
            index=(res[prev[i]] or 0)
            res[i]=index+(i-prev[i])*arr[i]
        maxs=sum(res)
        return maxs- mins


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.subarrayRanges(N, arr)
        print(res)
# } Driver Code Ends