#User function Template for python3

class Solution:

    #Function to find the largest number after k swaps.
    def solve(self,string, k,index, maxi):
        if k<=0 or index>=len(string)-1:
            return
        max_=string[index]
        for i in range(index+1, len(string)):
            if int(max_)<int(string[i]):
                max_=string[i]
        if string[index]!=max_:
            k-=1

        for i in range(index, len(string)):
            if max_==string[i]:
                string[index], string[i]=string[i],string[index]
                new_str="".join(string)
                if int(new_str)>int(maxi[0]):
                    maxi[0]=new_str
                self.solve(string, k, index+1, maxi)
                string[index], string[i]=string[i],string[index]

    def findMaximumNum(self,s,k):
        #code here
        maxi=[s]
        string=[char for char in s]
        index=0
        self.solve(string, k, index, maxi)
        return maxi[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob=Solution()
        print(ob.findMaximumNum(s,k))

# } Driver Code Ends