//{ Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function template for C++
#define MOD 1000000007
class Solution {
  public:
	int MinimumWalk(vector<vector<int>>&graph, int u, int v, int k){
	    // Code here
	    int n = graph.size();
	    vector<vector<int>> dp(n,vector<int>(k+1,0));
	    dp[v][0]=1;
	    
	    for(int x=1;x<=k;x++){
	        for(int i=0;i<n;i++){
	            for(int j=0;j<n;j++){
	                if(graph[i][j])
	                    dp[i][x] = (dp[i][x] + dp[j][x-1])%MOD;  
	            }
	        }
	    }
	    return dp[u][k];
	}

};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n;
		cin >> n;
		vector<vector<int>>graph(n, vector<int>(n,0));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				cin >> graph[i][j];
			}
		}
		int u, v, k;
		cin >> u >> v >> k;
		Solution obj;
		int ans = obj.MinimumWalk(graph, u, v, k);
		cout << ans << "\n";
	}
	return 0;
}
// } Driver Code Ends