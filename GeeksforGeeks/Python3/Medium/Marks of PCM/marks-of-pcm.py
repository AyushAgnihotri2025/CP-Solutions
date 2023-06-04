#User function Template for python3

class Solution:
    def customSort(self, phy, chem, math, N):
        # code here
        student_marks=[]
        for i in range(N):
            student_marks.append((phy[i],chem[i],math[i]))
        student_marks.sort(key = lambda x:(x[0],-x[1],x[2]))
        for i in range(N):
            phy[i]=student_marks[i][0]
            chem[i]=student_marks[i][1]
            math[i]=student_marks[i][2]
        return phy, chem , math

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input().strip())
        phy = []
        chem = []
        maths = []
        for i in range(n):
            marks = [int(x) for x in input().strip().split(" ")]
            phy.append(marks[0])
            chem.append(marks[1])
            maths.append(marks[2])
        
        ob=Solution()
        ob.customSort(phy, chem, maths, n)
        
        for i in range(n):
            print(phy[i], chem[i], maths[i])
        
# } Driver Code Ends