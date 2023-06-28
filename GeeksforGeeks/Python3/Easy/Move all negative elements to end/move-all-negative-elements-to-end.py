#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        A=[]
        B= []
        res = []
        for i in arr:
            if i > 0 :
                A.append(i)
            else:
                B.append(i)
        for i in range(len(A)):
            arr[i]=A[i]
        k=0
        for j in range(len(A),n):
            arr[j]=B[k]
            k+=1
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends