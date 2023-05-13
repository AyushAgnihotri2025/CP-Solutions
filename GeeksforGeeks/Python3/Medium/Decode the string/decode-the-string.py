#User function Template for python3

class Solution:
    def decodedString(self, s):
        # code here
        res=""
        st=[]
        for i in range(len(s)):
            if(s[i]==']'):
                temp=""
                while(st and st[-1]!='['):
                    temp+=st[-1]
                    st.pop()
                st.pop()
                temp=temp[::-1]
        
                subst=""
                while(st and ord(st[-1])>=48 and ord(st[-1])<=57):
                    subst+=st[-1]
                    st.pop()
                subst=subst[::-1]
            
                n=int(subst)
                for j in range(n):
                    for x in temp:
                        st.append(x)
            else:
                st.append(s[i])
        while(st):
            res+=st.pop()
        res=res[::-1]
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends