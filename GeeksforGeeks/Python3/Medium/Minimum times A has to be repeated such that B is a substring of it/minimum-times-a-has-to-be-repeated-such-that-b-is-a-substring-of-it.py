#User function Template for python3

class Solution:
    def minRepeats(self, A, B):
        # code here
        if A == B:
            return 1
        nA = len(A)
        nB = len(B)
        rep = A
        count = 1
        while (len(rep) < nB):
            rep += A
            count += 1
        if B in rep:
            return count
        else:
            rep += A
            count += 1
            if B in rep:
                return count
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A=input()
        B=input()
        
        ob = Solution()
        print(ob.minRepeats(A,B))
# } Driver Code Ends