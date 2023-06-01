#User function Template for python3

def number0f2s(n):
    #add Code here
    return str(n).count('2')
    
def numberOf2sinRange(n):
    
    #add code here
    count = 0
    for i in range(1, n+1):
        count += number0f2s(i)
    return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        print(numberOf2sinRange(n))
# } Driver Code Ends