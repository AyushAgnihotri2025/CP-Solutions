#User function Template for python3

class Solution:
    def findOnce(self,arr : list, n : int):
        # Complete this function
        for i in range(n-1):
            if i%2==0:
                if arr[i]!=arr[i+1]:
                    return arr[i]
        else:
            return arr[len(arr)-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))
# } Driver Code Ends