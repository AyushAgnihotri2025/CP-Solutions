//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    double waterOverflow(int K, int R, int C) {
        // code here
        vector<vector<double>> dp(K+1,vector<double>(K+1));
       dp[0][0]=K;
       for(int i=0;i<K;i++)
       {
           for(int j=0;j<=i;j++)
           {
               if(dp[i][j]>1.0)
               {
                   double spare = dp[i][j]-1.0;
                   dp[i][j]=1.0;
                   dp[i+1][j]+=spare/2.0;
                   dp[i+1][j+1]+= spare/2.0;
               }
           }
       }
       return dp[R-1][C-1];
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int K,R,C;
        
        cin>>K>>R>>C;

        Solution ob;
        cout << fixed << setprecision(6)<< ob.waterOverflow(K,R,C) << endl;
    }
    return 0;
}
// } Driver Code Ends