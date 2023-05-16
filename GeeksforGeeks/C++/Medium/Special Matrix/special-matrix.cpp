//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
public:
	int FindWays(int n, int m, vector<vector<int>>blocked_cells){
	    // Code here
	    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
	    int mod = 1000000007;
	    for(auto i: blocked_cells) dp[i[0] - 1][i[1] - 1] = -1;
	    for(int i = 0; i < m; i++) {
	        if(dp[0][i] == -1) break;
	        else dp[0][i] = 1;
	    }
	    for(int i = 0; i < n; i++) {
	        if(dp[i][0] == -1) break;
	        else dp[i][0] = 1;
	    }
	    for(int i = 1; i < n; i++) {
	        for(int j = 1; j < m; j++) {
	            if(dp[i][j] == -1) continue;
	            
	            if(dp[i - 1][j] != -1) 
	                dp[i][j] += dp[i - 1][j];
	            
	            if(dp[i][j - 1] != -1)
	                dp[i][j] += dp[i][j - 1];
	        }
	    }
	    return dp[n - 1][m - 1] == -1 ? 0 : dp[n - 1][m - 1] % mod;
	}
};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, m, k;
		cin >> n >> m >> k;
		vector<vector<int>>blocked_cells;
		for(int i = 0; i < k; i++){
			int x, y;
			cin >> x >> y;
			blocked_cells.push_back({x, y});
		}
		Solution obj;
		int ans = obj.FindWays(n, m, blocked_cells);
		cout << ans <<'\n';
	}
	return 0;
}
// } Driver Code Ends