#User function Template for python3

class Solution:
    def count_fives(self, num):
        result = 0
        i = 5
        while num // i > 0:
            result += num // i
            i *= 5
        return result

    def countZeroes(self, n):
        # code here
        l = 0
        r = n * 5
        while l <= r:
            mid = (l + r) // 2
            cnt = self.count_fives(mid)
            if cnt == n:
                return 5
            if cnt > n:
                r = mid - 1
            else:
                l = mid + 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ans = ob.countZeroes(N);
        print(ans)




# } Driver Code Ends