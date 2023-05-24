#User function Template for python3

class Solution:
    def transfigure(self, A, B): 
        # code here 
        if len(A) != len(B):
            return -1
        for c in set(A):
            if A.count(c) != B.count(c):
                return -1
        count=0
        i=len(A)-1
        j=len(B)-1
        while i>=0 and j>=0:
            if A[i]==B[j]:
                i-=1
                j-=1
            else:
                i-=1
                count+=1
        if count==len(A) :
            return -1
        else:
            return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        obj = Solution();
        print(obj.transfigure(A,B))


# } Driver Code Ends