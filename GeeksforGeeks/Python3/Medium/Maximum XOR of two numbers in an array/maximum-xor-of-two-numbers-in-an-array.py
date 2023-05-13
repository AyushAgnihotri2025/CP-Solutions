#User function Template for python3

from math import log

class Solution:
    def max_xor(self, arr, n):
        #code here
        try: l = int(log(max(arr), 2))
        except: l = 1
        
        mask, res = 0, 0
        
        for i in range(l, -1, -1):
            mask |= 1 << i
            
            S = set(mask & num for num in arr)
            
            temp = res | 1 << i
            
            for num in S:
                if num ^ temp in S:
                    res = temp
                    break
                
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		arr = list(map(int,input().split()))
		ob = Solution();
		print(ob.max_xor(arr,n))
	
# } Driver Code Ends