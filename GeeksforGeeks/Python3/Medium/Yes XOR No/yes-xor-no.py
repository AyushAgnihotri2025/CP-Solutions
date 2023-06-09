#User function Template for python3

class Solution:
    def yesXorNo(self, N, A, B):
        # code here
        xorr = 0
        obj = []
        for i,j in zip(A,B):
            obj.append(i^j)
            obj.append(j^i)
        map = {}
        for i in A:
            map[str(i)] = 0
        for i in B:
            map[str(i)] = 0
        for i in obj:
            if map.__contains__(str(i)):
                xorr+=1
        if xorr%2==0:
            return "Yes"
        return "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.yesXorNo(N,A,B))
# } Driver Code Ends