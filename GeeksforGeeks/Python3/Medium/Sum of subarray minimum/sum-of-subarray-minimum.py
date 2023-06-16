#User function Template for python3

class Solution:
    def sumSubarrayMins(self, n, arr):
        # Code here
        MOD = 10**9 + 7
        st = []
        left = [0] * n
        right = [n] * n
        for i in range(n):
            while st and arr[st[-1]] > arr[i]:
                st.pop()
            if st:
                left[i] = i - st[-1]
            else:
                left[i] = i + 1
            st.append(i)
        st = []
        for i in range(n-1, -1, -1):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st:
                right[i] = st[-1] - i
            else:
                right[i] = n - i
            st.append(i)
        res = 0
        for i in range(n):
            prod = (left[i] * right[i]) % MOD
            prod = (prod * arr[i]) % MOD
            res = (res + prod) % MOD
        return res % MOD

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.sumSubarrayMins(N, arr)
        print(res)
# } Driver Code Ends