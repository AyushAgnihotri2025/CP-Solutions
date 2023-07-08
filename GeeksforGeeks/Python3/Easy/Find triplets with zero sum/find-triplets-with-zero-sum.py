#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        arr.sort()
        if arr[0]>0:
            return 0
        elif arr[n-1]<0:
            return 0
        for i in range(n):
            first=arr[i]
            left=i+1
            right=n-1
            while left<right:
                su=first+arr[left]+arr[right]
                if su>0:
                    right-=1
                elif su<0:
                    left+=1
                elif su==0:
                    return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends