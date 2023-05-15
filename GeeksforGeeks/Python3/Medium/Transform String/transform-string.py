#Back-end complete function Template for Python 3

class Solution:
    def transform(self, A, B): 
        #code here.
        d = dict()
        for ch in A:
            d[ch] = d.get(ch, 0) + 1
        for ch in B:
            d[ch] = d.get(ch, 0) - 1
        if any(d.values()):
            return -1
    
        j = len(B) - 1
        for ch in A[::-1]:
            if B[j] == ch:
                j -= 1
        return j + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        ob = Solution()
        print(ob.transform(A,B))
# } Driver Code Ends