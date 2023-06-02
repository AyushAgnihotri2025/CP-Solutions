#User function Template for python3

import math

def fact (n) : 
    #Complete the function
    return str(math.factorial(n))[0], math.floor(math.log(math.factorial(n))/math.log(10))

#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    ans = fact(n)
    print(*ans)




# } Driver Code Ends