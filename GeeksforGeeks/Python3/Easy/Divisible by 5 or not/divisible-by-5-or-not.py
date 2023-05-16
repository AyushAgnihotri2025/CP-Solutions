#User function Template for python3

class Solution:
    def isDivisibleBy5(self, Bin):
        # code here
        return "Yes" if (int(Bin, 2) % 5 == 0) else "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Bin = input()

        solObj = Solution()

        print(solObj.isDivisibleBy5(Bin))
# } Driver Code Ends