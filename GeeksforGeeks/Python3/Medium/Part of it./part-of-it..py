#User function Template for python3

class Solution:
    def isPart (self, n):
        #complete the function here
        n += 2
        i = 2
        while(i*i <= n):
            if (n%i==0):
                return "No"
            i+=1
        return "Yes"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.isPart(n))
# } Driver Code Ends