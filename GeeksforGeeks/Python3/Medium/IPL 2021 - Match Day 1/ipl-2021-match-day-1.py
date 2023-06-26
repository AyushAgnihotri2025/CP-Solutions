#User function Template for python3

class Solution:
    def findPoint(self, A, B, C):
        # code here
        return min([C[0] + B[0] - A[0], C[1] + B[1] - A[1]], [C[0] + A[0] - B[0], C[1] + A[1] - B[1]],[A[0] + B[0] - C[0], A[1] + B[1] - C[1]])

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A = []
        B = []
        C = []
        input1 = [int(x) for x in input().strip().split(" ")]
        A.append(input1[0])
        A.append(input1[1])
        input2 = [int(x) for x in input().strip().split(" ")]
        B.append(input2[0])
        B.append(input2[1])
        input3 = [int(x) for x in input().strip().split(" ")]
        C.append(input3[0])
        C.append(input3[1])
        
        ob=Solution()
        ans = ob.findPoint(A, B, C)
        print("{:.6f}".format(ans[0]),"{:.6f}".format(ans[1]))
        
# } Driver Code Ends