#User function Template for python3

class Solution:
    def nullPoints(self, n, a, getAnswer):
        # Your code goes here
        for i in range(n-1):
            low = a[i]
            high = a[i+1]
            while round(low,2) != round(high,2):
                mid = (low + high) /2
                force = sum(1/(x-mid) for x in a)
                if force == 0:
                    low = mid
                    break
                elif force < 0:
                    low = mid
                else:
                    high = mid
            getAnswer[i] = round(low,2)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        getAnswer = [0]*n
        ob=Solution()
        ob.nullPoints(n, a, getAnswer)
        
        for i in range(0,n-1):
            print("{:.2f}".format(getAnswer[i]), end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends