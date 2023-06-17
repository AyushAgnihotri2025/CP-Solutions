#User function Template for python3
class Solution:
    def nxtHighUsingAtMostOneSwap(self, num): 
        # code here
        a = [c for c in num]
        n = len(num)
        marked = [-1] * 10
        marked[ord(a[n-1]) - ord('0')] = n - 1
        for i in range(n-2, -1, -1):
            pos = -1
            for j in range(ord(a[i]) - ord('0') + 1, 10):
                if marked[j] != -1 and (pos == -1 or pos < marked[j]):
                    pos = marked[j]
            if pos != -1:
                a[pos], a[i] = a[i], a[pos]
                num2 = ''.join(a)
                return num2
            marked[ord(a[i]) - ord('0')] = i
        return "-1"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        num = input().strip()
        obj = Solution()
        print(obj.nxtHighUsingAtMostOneSwap(num))
# } Driver Code Ends