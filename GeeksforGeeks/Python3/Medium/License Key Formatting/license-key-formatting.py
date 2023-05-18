#User function Template for python3
from collections import deque
class Solution:
    def ReFormatString(self,S, K):
        #code here
        s = deque()
        cnt = 0
        for i in range(len(S)-1, -1, -1):
            if S[i] != '-':
                s.appendleft(S[i].upper())
                cnt += 1
                if cnt == K:
                    s.appendleft("-")
                    cnt = 0
        return "".join(s).lstrip("-")


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import atexit
import io
import sys
from collections import defaultdict
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
        s=str(input())
        k=int(input())
        obj = Solution()
        print(obj.ReFormatString(s, k))
# } Driver Code Ends