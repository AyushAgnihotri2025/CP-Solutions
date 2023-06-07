#User function Template for python3
from queue import LifoQueue

class Solution:
    def isSumString(ob, S):
        # code here 
        n = len(S)
        for l in range(1, n):
            sub_arr = int(S[n-l:])
            if ob.is_sum_string_sub(S,n-l,sub_arr, None) == 1:
                return 1
        return 0

    def is_sum_string_sub(self, S, limit, sub_arr, sub_1):
        sub_2 = 0
        if sub_1 is None:
            sub_1 = 0
            for l_1 in range(1,limit+1):
                sub_1 = int(S[limit-l_1:limit])
                if sub_1 > sub_arr:
                    return 0
                for l_2 in range(1,limit-l_1+1):
                    sub_2 = int(S[limit-l_1-l_2:limit-l_1])
                    if sub_1 + sub_2 > sub_arr:
                        break
                    if sub_1 + sub_2 == sub_arr:
                        if limit-l_1-l_2 == 0:
                            return 1
                        if self.is_sum_string_sub(S,limit-l_1-l_2,sub_1,sub_2) == 1:
                            return 1
        else:
            for l_2 in range(1,limit+1):
                    sub_2 = int(S[limit-l_2:limit])
                    if sub_1 + sub_2 > sub_arr:
                        break
                    if sub_1 + sub_2 == sub_arr:
                        if limit-l_2 == 0:
                            return 1
                        if self.is_sum_string_sub(S,limit-l_2,sub_1,sub_2) == 1:
                            return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        
        print(ob.isSumString(S))
# } Driver Code Ends