class Solution:
    def binTreeSortedLevels (self,arr, n):
        #code here.
        li=[]
        i=0
        level=0
        while i<n:
            dumm=[]
            if level==0:
                li.append([arr[i]])
                i+=1
                level+=1
            else:
                size=2**level
                if i+size<n:
                    dumm.extend(arr[i:i+size])
                    dumm.sort()
                    li.append(dumm)
                    i+=size
                    level+=1
                else:
                    dumm.extend(arr[i:])
                    dumm.sort()
                    li.append(dumm)
                    break
        return li

#{ 
 # Driver Code Starts

t = int (input ())
for tc in range (t):
    n = int (input ())
    arr = list(map(int, input().split()))
    
    ob = Solution()
    res = ob.binTreeSortedLevels (arr, n)
    
    for i in range (len (res)):
        for j in range (len (res[i])):
            print (res[i][j], end = " ")
        print ()
        
# Contributed By: Pranay Bansal
# } Driver Code Ends