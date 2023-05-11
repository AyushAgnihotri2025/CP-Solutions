#User function Template for python3

from bisect import bisect_left

class Solution:
    def maxSumLis(self, Arr, n):
        # code here
        lis = []
        sum = 0
        lis_sum = [0] * (n + 1)
        lis_sum[0] = 0
        for i in range(n):
            sum += Arr[i]
            index = bisect_left(lis, Arr[i])
            if index == len(lis):
                lis.append(Arr[i])
            else:
                lis[index] = Arr[i]
            lis_sum[index + 1] = lis_sum[index] + Arr[i]
        return sum - lis_sum[len(lis)]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        n = int(input())
        Arr = input().split()
        for itr in range(n):
            Arr[itr] = int(Arr[itr])
        
        ob = Solution()
        print(ob.maxSumLis(Arr, n))
# } Driver Code Ends