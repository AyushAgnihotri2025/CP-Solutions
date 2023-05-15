#User function Template for python3

class Solution:
    def waysToIncreaseLCSBy(self,N1,S1,N2,S2):
        # code here
        m = len(S1)
        n = len(S2)
    
        # Fill positions of each character in vector
        # vector<int> position[M];
        position = [[] for i in range(26)]
        for i in range(1, n+1, 1):
            position[ord(S2[i-1])-97].append(i)
    
        # Initializing 2D array by 0 values
        lcsl = [[0 for i in range(n+2)] for j in range(m+2)]
        lcsr = [[0 for i in range(n+2)] for j in range(m+2)]
    
        # Filling LCS array for prefix substrings
        for i in range(1, m+1, 1):
            for j in range(1, n+1,1):
                if (S1[i-1] == S2[j-1]):
                    lcsl[i][j] = 1 + lcsl[i-1][j-1]
                else:
                    lcsl[i][j] = max(lcsl[i-1][j],
                                    lcsl[i][j-1])
    
        # Filling LCS array for suffix substrings
        for i in range(m, 0, -1):
            for j in range(n, 0, -1):
                if (S1[i-1] == S2[j-1]):
                    lcsr[i][j] = 1 + lcsr[i+1][j+1]
                else:
                    lcsr[i][j] = max(lcsr[i+1][j],
                                    lcsr[i][j+1])
    
            # Looping for all possible insertion positions
            # in first string
        ways = 0
        for i in range(0, m+1,1):
            # Trying all possible lower case characters
            for C in range(0, 26,1):
                # Now for each character, loop over same
                # character positions in second string
                for j in range(0, len(position[C]),1):
                    p = position[C][j]
    
                    # If both, left and right substrings make
                    # total LCS then increase result by 1
                    if (lcsl[i][p-1] + lcsr[i+1][p+1] == lcsl[m][n]):
                        ways += 1
                        break
        return ways


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N1,N2 = input().split()
        N1 = int(N1)
        N2 = int(N2)
        
        S1,S2 = input().split()
        
        ob = Solution()
        print(ob.waysToIncreaseLCSBy(N1,S1,N2,S2))
# } Driver Code Ends