#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
from typing import List

class Solution:
    def kthPermutation(self, n : int, k : int) -> str:
        # code here
        ans = []
        def compute(n, k):
            from math import factorial as fact
            if n == 0:
                return
            acc = 0
            for i in range(1, 10):
                if i not in ans:
                    f = fact(n-1)
                    if acc + f < k:
                        acc += f
                    else:
                        ans.append(i)
                        break
            compute(n-1, k-acc)
        compute(n, k)
        return "".join(map(str, ans))


#{ 
 # Driver Code Starts.
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N, K = map(int, input().split())
        
        obj = Solution()
        res = obj.kthPermutation(N, K)
        
        print(res)
        

# } Driver Code Ends