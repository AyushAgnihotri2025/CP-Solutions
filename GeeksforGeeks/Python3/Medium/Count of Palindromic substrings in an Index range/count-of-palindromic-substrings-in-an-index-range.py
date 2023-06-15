#User function Template for python3

def countPalinInRange (n, s, q1, q2):
    # your code here
    count=0
    temp1=min(q1,q2)
    temp2=max(q1,q2)
    q1=temp1
    q2=temp2
    for mid in range(q1,q2+1):
        count=count+1
        start=mid-1
        end=mid+1
        while start>=q1 and end<=q2:
            if s[start]==s[end]:
                count=count+1
                start=start-1
                end=end+1
            else:
                break
    for i in range(q1,q2):
        left=i
        right=left+1
        while left>=q1 and right<=q2:
            if s[left]==s[right]:
                left=left-1
                right=right+1
                count=count+1
            else:
                break
    return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    s = input ()
    q1, q2 = list(map(int, input().split()))
    print (countPalinInRange (n, s, q1, q2))
    
# Contributed By: Pranay Bansal

# } Driver Code Ends