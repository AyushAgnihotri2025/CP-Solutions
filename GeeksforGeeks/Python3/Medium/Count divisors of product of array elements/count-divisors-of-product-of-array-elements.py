#User function Template for python3

class Solution:
    def countDivisorsMult(self, a, n):
        #Code here
        prime_freq = {}
        for i in range(n):
            x = a[i]
            j = 2
            while j*j <= x:
                while x % j == 0:
                    prime_freq[j] = prime_freq.get(j, 0) + 1
                    x //= j
                j += 1
            if x > 1:
                prime_freq[x] = prime_freq.get(x, 0) + 1
        count = 1
        for freq in prime_freq.values():
            count *= freq + 1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        print(Solution().countDivisorsMult(a, n))
        
        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends