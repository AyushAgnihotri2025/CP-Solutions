//{ Driver Code Starts
#include<bits/stdc++.h>
#define MAX 1000
using namespace std;
 
int maxSubsequenceSubstring(string x, string y, int n, int m);
 
// Driver Program
int main()
{
    int t;
    cin>>t;
    while(t--){
        int n,m;
        string x,y;
        cin>>n>>m;
        cin>>x>>y;
        cout<<maxSubsequenceSubstring(x,y,n,m)<<"\n";
    }
    return 0;
}
// } Driver Code Ends

int dp[1001][1001];

int maxSubsequenceSubstring(string X, string Y, int N, int M){
    //code
    memset(dp,0,sizeof(dp));
    int maxSubstring=0;
    for(int i=1;i<N+1;++i){
        for(int j=1;j<M+1;++j){
            if(X[i-1]==Y[j-1]) dp[i][j]=1+dp[i-1][j-1];
            else dp[i][j]=dp[i-1][j];
        }
    }
    for(int i=0;i<N+1;++i){
        for(int j=0;j<M+1;++j){
            maxSubstring=max(maxSubstring,dp[i][j]);
        }
    }
    return maxSubstring;
}