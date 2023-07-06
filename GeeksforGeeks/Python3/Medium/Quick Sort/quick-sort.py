#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low<high:
            pivot=self.partition(arr,low,high)
            self.quickSort(arr,low,pivot-1)
            self.quickSort(arr,pivot+1,high)

    def partition(self,arr,low,high):
        # code here
        pivot=low
        i=low
        j=i+1
        while j<=high:
            if arr[j]>=arr[pivot]:
                j+=1
            else:
                i=i+1
                arr[i],arr[j]=arr[j],arr[i]
                j+=1
        arr[i],arr[pivot]=arr[pivot],arr[i]
        return i

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends