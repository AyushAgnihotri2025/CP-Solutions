#User function Template for python3

class Solution:    
    def Rearrange(self, a, n, answer):
        #Code Here
        a.sort()
        start=0
        end=n-1
        for i in range(n):
            if i%2==0:
                answer[i]=a[start]
                start+=1
            else:
                answer[i]=a[end]
                end-=1
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        answer = [0 for x in range(n)]
        ob = Solution()
        ob.Rearrange(a, n, answer)
        print(*answer)

        T -= 1


if __name__ == "__main__":
    main()






# } Driver Code Ends