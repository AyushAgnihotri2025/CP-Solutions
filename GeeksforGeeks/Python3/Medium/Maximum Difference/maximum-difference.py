class Solution:
    # Your task is to complete this function
    # Function should return an integer denoting the required answer
    def findMaxDiff(self, arr, n):
        # Code here
        left = [0]*n
        right = [0]*n
        l, r = [], []
        r.append(0)
        l.append(0)
        for i in range(n-1,-1,-1):
            while(arr[i]<=r[-1]):
                r.pop()
            right[i] = r[-1]
            r.append(arr[i])
        for i in range(0,n):
            while(arr[i]<=l[-1]):
                l.pop()
            left[i] = l[-1]
            l.append(arr[i])
        ans = 0
        for i in range(n):
            val = abs(left[i] - right[i])
            ans = max(ans,val)
        return ans

#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.findMaxDiff(arr, n))
#Contributed By: Harshit Sidhwa
# } Driver Code Ends