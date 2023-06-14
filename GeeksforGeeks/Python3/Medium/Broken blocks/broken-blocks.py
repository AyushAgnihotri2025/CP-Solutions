#User function Template for python3

class Solution:
	def MaxGold(self, matrix):
		# Code here
        l=len(matrix)
        o=len(matrix[0])
        if l==1:
            r= max(matrix[0])
            if r==-1:
                return 0
            return r
        if o==1:
            p=matrix[0][0]
            if matrix[0][0]==-1:
                return 0
            for h in range(1,l):
                if matrix[h][0]==-1:
                    return p
                matrix[h][0]+=matrix[h-1][0]
                p=matrix[h][0]
            return p
        for h in range(l-2,-1,-1):
            for g in range(o):
                m=0
                if matrix[h][g]==-1:
                    continue
                if g==0 and h+1<l and g+1<o:
                    m=max(m,matrix[h+1][g],matrix[h+1][g+1])
                elif g==o-1 and h+1<l and g-1<o and g-1>=0:
                    m=max(m,matrix[h+1][g],matrix[h+1][g-1])
                elif h+1<l  and g+1<o and g>0 and g<o-1 :
                    m=max(m,matrix[h+1][g],matrix[h+1][g+1],matrix[h+1][g-1])
                matrix[h][g]+=m
        r= max(matrix[0])
        if r==-1:
            return 0
        return r

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m, n = input().split()
		m = int(m); n = int(n);
		matrix = []
		for _ in range(m):
			cur = list(map(int, input().split()))
			matrix.append(cur)
		obj = Solution()
		ans = obj.MaxGold(matrix)
		print(ans)

# } Driver Code Ends