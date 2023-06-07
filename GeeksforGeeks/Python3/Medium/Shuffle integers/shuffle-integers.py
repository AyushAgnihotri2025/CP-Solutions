class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        for i in range(n//2):
           arr.append(arr[i])
           arr.append(arr[n//2+i])
        arr[:] = arr[n:]
        return arr

#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends