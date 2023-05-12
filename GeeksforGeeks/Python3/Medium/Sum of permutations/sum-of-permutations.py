#Function should return an integer
#You may use python modules
from itertools import permutations

MOD = 10**9+7
def getSum(n, arr):
    #Code here
    for i in range(0,n):
        arr[i]=str(arr[i])
    a=0
    for c in permutations(arr,n):
        k=int(''.join(c))
        a=a+k
    return a%MOD


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        arr = list(map(int, input().strip().split()))
        print(getSum(n, arr))
#contributed By: Harshit Sidhwa
# } Driver Code Ends