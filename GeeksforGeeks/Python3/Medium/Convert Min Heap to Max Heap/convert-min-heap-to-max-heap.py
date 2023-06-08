#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def convertMinToMaxHeap(self, N, arr):
        # Code here
        self.helper(N, arr)
        return arr
        
    def helper(self, N, arr):
        for i in range(N//2 -1 , -1, -1):
            self.purculate_down(i, arr)
    
    def purculate_down(self, i, arr):
        if i >= len(arr):
            return
        l_c = 2 * i + 1
        r_c = 2 * i + 2
        if l_c >= len(arr):
            return
        l_val = arr[l_c]
        r_val = -1
        if r_c < len(arr):
            r_val = arr[r_c]
        if arr[i] > l_val and arr[i] > r_val:
            return
        else:
            if l_val < r_val:
                arr[i], arr[r_c] = arr[r_c], arr[i]
                self.purculate_down(r_c, arr)
            else:
                arr[i], arr[l_c] = arr[l_c], arr[i]
                self.purculate_down(l_c, arr)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.convertMinToMaxHeap(N, arr)
        for val in arr:
            print(val, end = ' ')
        print()
# } Driver Code Ends