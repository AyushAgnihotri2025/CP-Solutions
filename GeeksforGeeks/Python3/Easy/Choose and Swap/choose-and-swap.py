#User function Template for python3


class Solution:
    def chooseandswap (self, a):
        # code here
        arr = list(A)
        freq = [0] * 26
        for c in arr:
            freq[ord(c) - ord('a')] += 1
    
        for i in range(len(arr)):
            curr = arr[i]
            for j in range(ord(curr) - ord('a')):
                if freq[j] > 0:
                    return self.replace(arr, curr, chr(ord('a') + j))
            freq[ord(curr) - ord('a')] = 0
    
        return A
    
    def replace(self, arr, a, b):
        for i in range(len(arr)):
            if arr[i] == a:
                arr[i] = b
            elif arr[i] == b:
                arr[i] = a
        return ''.join(arr)






#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)


# } Driver Code Ends