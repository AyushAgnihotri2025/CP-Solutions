#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        #complete the function here
        ans=999999
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if arr[low]<=arr[high]:
                ans=min(ans,arr[low])
                break
            if arr[low]<=arr[mid]:
                ans=min(ans,arr[low])
                low=mid+1
            else:
                ans=min(ans,arr[mid])
                high=mid-1
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends