# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equalSum(self,A, N):
        # Your code here
        if len(A)==1:
            return 1
        total=sum(A)
        count=0
        for i in range(N):
            if total-A[i]==2*count:
                return i+1
            count+=A[i]    
        return -1   



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equalSum(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends