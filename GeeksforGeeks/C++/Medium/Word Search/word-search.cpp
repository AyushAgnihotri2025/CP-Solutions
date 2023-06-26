//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;



// } Driver Code Ends
//User function Template for C++

class Solution {
public:
    bool solve(int i, int j, vector<vector<char>>&m, string w, int len){
        if(len == w.length()){
            return true;
        }
        if(i < 0 || j < 0 || i > m.size()-1 || j > m[0].size()-1){
            return false;
        }
        if(m[i][j] != w[len]){
            return false;
        }
        m[i][j] = '+';
        bool ans = solve(i+1,j,m,w,len+1)||solve(i-1,j,m,w,len+1)||solve(i,j-1,m,w,len+1)||solve(i,j+1,m,w,len+1);
        m[i][j] = w[len];
        return ans;
    }

    bool wordSearch(vector<vector<char>>& m, string w) {
        //code here
        for(int i=0; i<m.size(); i++){
            for(int j=0; j<m[0].size(); j++){
                if(m[i][j] == w[0] && solve(i,j,m,w,0)){
                    return true;
                }
            }
        }
        return false;
    }
};

//{ Driver Code Starts.
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        vector<vector<char>> mat(n,vector<char>(m));
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                cin>>mat[i][j];
            }
        }
        string str; cin>>str;
        Solution ob;
        auto ans=ob.wordSearch(mat,str);
        cout<<ans<<"\n";
    }
    return 0;
}

// } Driver Code Ends