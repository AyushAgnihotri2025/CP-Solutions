#User function Template for python3

class Solution:
	def idToShortURL(self,n):
		# code here
        checker = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        URL = ""
        while n > 0:
            res = n % 62
            n = n // 62
            URL += checker[res]
        return URL[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def shortURLToId(shortURL):
    id = 0
    for i in shortURL:
        val_i = ord(i)
        if (val_i >= ord('a') and val_i <= ord('z')):
            id = id * 62 + val_i - ord('a')
        elif (val_i >= ord('A') and val_i <= ord('Z')):
            id = id * 62 + val_i - ord('A') + 26
        else:
            id = id * 62 + val_i - ord('0') + 52
    return id


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        url = ob.idToShortURL(n)
        print(url)
        print(shortURLToId(url))
        tc -= 1

# } Driver Code Ends