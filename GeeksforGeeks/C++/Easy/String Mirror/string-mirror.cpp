//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    string stringMirror(string str){
        // Code here
        string ans="";
        ans+=str[0];
        int idx=-1;
        char prev=str[0];
        for(int i=1;i<str.length();i++)
        {
            if(str[i]<=prev && (idx+1==i))
            {
                ans+=str[i];
                prev=str[i];
                idx=i;
            }
            else if(i==1)
            {
                if(str[i]<prev)
                {
                    ans+=str[i];
                    prev=str[i];
                    idx=i;
                }
            }
        }
        string rev=ans;
        reverse(rev.begin(),rev.end());
        ans+=rev;
        return ans;
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        string str;
        cin>>str;
        Solution ob;
        string res=ob.stringMirror(str);
        cout<<res<<endl;
    }
}
// } Driver Code Ends