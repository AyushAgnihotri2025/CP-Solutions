#User function Template for python3

class Solution:
    def removeDuplicate(self, A, N):
        # code here
        d, ans = {}, []
        for i in A:
            if i not in d:
                d[i]=1
                ans.append(i)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        getAnswer = ob.removeDuplicate(a, n)
        
        print(*getAnswer)

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends