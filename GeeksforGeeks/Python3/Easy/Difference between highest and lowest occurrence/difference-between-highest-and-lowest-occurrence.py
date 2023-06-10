#User function Template for python3

class Solution:
    def findDiff(self, a, n):
        #Code here
        d = {}
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return max(d.values())-min(d.values())

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [x for x in input().strip().split()]
        
        print(Solution().findDiff(a, n))
        
        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends