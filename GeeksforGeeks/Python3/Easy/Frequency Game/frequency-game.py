#User function Template for python3

from collections import Counter

def LargButMinFreq(arr,n):
    #code here
    s=dict(Counter(arr))
    x=min(s.values())
    maxi=0
    for i in s:
        if(s[i]==x):
            maxi=max(maxi,i)
    return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends