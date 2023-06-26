#User function Template for python3
class Solution:
	def leftMostDiv(self, p, q):
		# code here
		e=p**q
        if len(str(e))>18: e=str(e)[0:10]
        for i in str(e):
            if i!='0':
                if int(e) % int(i)==0:
                    return int(i)
        return -1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		p,q = input().split()
		p=int(p)
		q=int(q)
		ob = Solution();
		print(ob.leftMostDiv(p, q))

# } Driver Code Ends