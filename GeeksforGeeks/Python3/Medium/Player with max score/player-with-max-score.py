#User function Template for python3

class Solution:
    def is1winner (self, N, arr):
        # code here
        if N % 2 ==0:
            return True
        odd_sum = 0
        even_sum = 0
        for idx in range(0,N-1):
            if idx % 2 ==0:
                odd_sum = odd_sum + arr[idx]
            else:
                even_sum = even_sum + arr[idx]
        if odd_sum >= even_sum:
            even_sum =even_sum +arr[0]
            if even_sum>=odd_sum:
                return True
        else:
            odd_sum =odd_sum +arr[0]
            if odd_sum>even_sum:
                return Ture
        odd_sum = 0
        even_sum = 0
        for idx in range(1,N):
            if idx % 2 ==0:
                odd_sum = odd_sum + arr[idx]
            else:
                even_sum = even_sum + arr[idx]
        if odd_sum >= even_sum:
            even_sum =even_sum +arr[N-1]
            if even_sum>=odd_sum:
                return True
        else:
            odd_sum =odd_sum +arr[N-1]
            if odd_sum>even_sum:
                return Ture
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
    
        ob = Solution()
        if ob.is1winner(N, arr) == True:
            print(1)
        else :
            print(0)
        

# } Driver Code Ends