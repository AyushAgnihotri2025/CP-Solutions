#User function Template for python3

class Solution:
    def maxSumBitonicSubArr(self, a, n):
        #Code here
        a = list(map(int, a))
        maxi = a[0]
        i = 0
        while i < n-1:
            if a[i] == a[i+1]:
                i += 1
            summa = a[i]
            while i < n-1 and a[i] < a[i+1]:
                i += 1
                summa += a[i]
            while i < n-1 and a[i] > a[i+1]:
                i += 1
                summa += a[i]
            maxi = max(maxi, summa)
        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [x for x in input().strip().split()]
        
        print(Solution().maxSumBitonicSubArr(a, n))
        
        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends