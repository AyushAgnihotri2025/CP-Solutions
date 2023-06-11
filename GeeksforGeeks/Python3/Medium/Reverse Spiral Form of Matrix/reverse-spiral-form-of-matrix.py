#User function Template for python3
class Solution:
	def reverseSpiral(self, R, C, a):
		# code here
        top,left,bottom,right=0,0,R-1,C-1
        list1=[]
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                list1.append(a[top][i])
            top+=1
            for i in range(top,bottom+1):
                list1.append(a[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    list1.append(a[bottom][i])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    list1.append(a[i][left])
                left+=1
        return list1[::-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C=[int(x) for x in input().split()]
        a=[[0]*C for c in range(R)]
        arr=input().split()
        for i in range(R*C):
            a[i//C][i%C]=int(arr[i])
            
        ob=Solution()
        ans=ob.reverseSpiral(R,C,a)
        for i in range(len(ans)):
            print(ans[i],end=" ")
            
        print()
# } Driver Code Ends