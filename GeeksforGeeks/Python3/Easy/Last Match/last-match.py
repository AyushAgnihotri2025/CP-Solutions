#User function Template for python3
class Solution:
    def findLastOccurence(self, A, B):
        # code here
        for i in range(len(A)-1,-1,-1):
            if A[i]==B[0] and A[i:i+len(B)]==B:
                return i+1
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        A = input()
        B= input()

        ob = Solution()
        print(ob.findLastOccurence(A,B))
# } Driver Code Ends