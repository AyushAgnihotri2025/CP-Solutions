#User function Template for python3
class Solution:
	def kSubstrConcat(self, n, s, k):
		# Your Code Here
        if n % k != 0:
            return 0
        pat = s[0:k]
        cnt, cnt2 = 0, 0
        pat2 = ""
        for i in range(0, n, k):
            if pat == s[i:i+k]:
                cnt += 1
            elif pat2 == "":
                pat2 = s[i:i+k]
                cnt2 += 1
            elif pat2 == s[i:i+k]:
                cnt2 += 1
        if (cnt <= 1 or cnt2 <= 1) and cnt + cnt2 == n // k:
            return 1
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		s = input()
		k = int(input())
		ob = Solution()
		print(ob.kSubstrConcat(n,s,k))

# } Driver Code Ends