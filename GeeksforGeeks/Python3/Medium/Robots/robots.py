#User function Template for python3

class Solution:
    def moveRobots (self, s1, s2):
        # code here
        l = len(s1)
        m = len(s2)
        i = 0
        j = 0
        while i<l and j<m:
            while i<l and s1[i]=='#':
                i += 1
            while j<m and s2[j]=='#':
                j += 1
            if i==l and j==l:
                return 'Yes'
            if (i==l and j<m) or (j==m and i<l) or (s1[i]!=s2[j]) or (s1[i]=='A' and i<j) or (s2[i]=='B' and j<i):
                return 'No'
            i += 1
            j += 1
        return 'Yes'

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s1 = input()
        s2 = input()

        ob = Solution()
        print(ob.moveRobots(s1, s2))

# } Driver Code Ends