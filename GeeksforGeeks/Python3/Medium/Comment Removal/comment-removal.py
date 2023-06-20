#User function Template for python3
class Solution:
	def removeComments (self, code):
		# your code here
		n=len(code)
        i=0
        flag=0
        while(i<len(code)):
            n=len(code)
            if(code[i]=="/" and i+1<n and code[i+1]=="/" and flag==0):
                s=i
                flag=1
                i+=2
            elif(code[i]=="\\" and i+1<n and code[i+1]=="n" and flag==1):
                e=i+2
                flag=0
                code=code[0:s]+code[e:]
                i=s
            elif(code[i]=="/" and i+1<n and code[i+1]=="*" and flag==0):
                s=i
                flag=2
                i+=2
            elif(code[i]=="*" and i+1<n and code[i+1]=="/" and flag==2):
                e=i+2
                flag=0
                code=code[0:s]+code[e:]
                i=s
            else:
                i+=1
        return code


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		print (ob.removeComments (s))

	# Contributed By: Pranay Bansal
# } Driver Code Ends