//{ Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution
{
    public:
    int countSubstring(string S)
    {
        int ans=0;
        for(int i=0;i<S.size();i++){
            int c1=0,c2=0;
            for(int j=i;j<S.size();j++){
                if(S[j]>='a') //if lower
                    c1++;
                else
                    c2++;
                if(c1==c2)
                    ans++;
            }
        }
        return ans;
    }
};

//{ Driver Code Starts.
int main()
{

    int t;
    cin>>t;
    while(t--)
    {
        string S;
        cin>>S;
        Solution obj;
        cout<<obj.countSubstring(S)<<endl;
    }
}  
// } Driver Code Ends